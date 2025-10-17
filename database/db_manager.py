"""
Database Manager
Handles SQLite database operations for storing resumes, candidates, and matches
"""
import sqlite3
import json
from datetime import datetime
from pathlib import Path
from config import Config


class DatabaseManager:
    """Manage database operations for the application"""
    
    def __init__(self):
        """Initialize database connection"""
        self.db_path = Config.DATABASE_PATH
        # Ensure data directory exists
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
    
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
    
    def init_db(self):
        """Initialize database schema"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Candidates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                resume_text TEXT NOT NULL,
                data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Job postings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_postings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                job_description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Match results table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS match_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                candidate_id INTEGER NOT NULL,
                score REAL NOT NULL,
                justification TEXT,
                match_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (job_id) REFERENCES job_postings (id),
                FOREIGN KEY (candidate_id) REFERENCES candidates (id)
            )
        """)
        
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")
    
    def save_candidate(self, filename, resume_text, candidate_data):
        """
        Save candidate information to database
        
        Args:
            filename: Original filename
            resume_text: Extracted text from resume
            candidate_data: Structured candidate information
            
        Returns:
            ID of inserted candidate
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO candidates (filename, resume_text, data)
            VALUES (?, ?, ?)
        """, (filename, resume_text, json.dumps(candidate_data)))
        
        candidate_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return candidate_id
    
    def get_candidate(self, candidate_id):
        """
        Get candidate by ID
        
        Args:
            candidate_id: ID of candidate
            
        Returns:
            Candidate data or None
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, filename, resume_text, data, created_at
            FROM candidates
            WHERE id = ?
        """, (candidate_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row['id'],
                'filename': row['filename'],
                'resume_text': row['resume_text'],
                'data': json.loads(row['data']),
                'created_at': row['created_at']
            }
        return None
    
    def get_all_candidates(self):
        """
        Get all candidates from database
        
        Returns:
            List of candidate dictionaries
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, filename, resume_text, data, created_at
            FROM candidates
            ORDER BY created_at DESC
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        candidates = []
        for row in rows:
            candidates.append({
                'id': row['id'],
                'filename': row['filename'],
                'resume_text': row['resume_text'],
                'data': json.loads(row['data']),
                'created_at': row['created_at']
            })
        
        return candidates
    
    def save_job_matching(self, job_title, job_description, match_results):
        """
        Save job posting and match results
        
        Args:
            job_title: Title of the job
            job_description: Job description text
            match_results: List of match result dictionaries
            
        Returns:
            ID of inserted job posting
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Save job posting
        cursor.execute("""
            INSERT INTO job_postings (job_title, job_description)
            VALUES (?, ?)
        """, (job_title, job_description))
        
        job_id = cursor.lastrowid
        
        # Save match results
        for result in match_results:
            cursor.execute("""
                INSERT INTO match_results 
                (job_id, candidate_id, score, justification, match_data)
                VALUES (?, ?, ?, ?, ?)
            """, (
                job_id,
                result['candidate_id'],
                result['score'],
                result['justification'],
                json.dumps(result)
            ))
        
        conn.commit()
        conn.close()
        
        return job_id
    
    def get_job_history(self):
        """
        Get job matching history
        
        Returns:
            List of job postings with match counts
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                jp.id,
                jp.job_title,
                jp.job_description,
                jp.created_at,
                COUNT(mr.id) as match_count,
                AVG(mr.score) as avg_score
            FROM job_postings jp
            LEFT JOIN match_results mr ON jp.id = mr.job_id
            GROUP BY jp.id
            ORDER BY jp.created_at DESC
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        jobs = []
        for row in rows:
            jobs.append({
                'id': row['id'],
                'job_title': row['job_title'],
                'job_description': row['job_description'],
                'created_at': row['created_at'],
                'match_count': row['match_count'],
                'avg_score': round(row['avg_score'], 2) if row['avg_score'] else 0
            })
        
        return jobs
    
    def get_job_matches(self, job_id):
        """
        Get all matches for a specific job
        
        Args:
            job_id: ID of the job posting
            
        Returns:
            List of match results with candidate information
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                mr.id,
                mr.score,
                mr.justification,
                mr.match_data,
                mr.created_at,
                c.id as candidate_id,
                c.filename,
                c.data as candidate_data
            FROM match_results mr
            JOIN candidates c ON mr.candidate_id = c.id
            WHERE mr.job_id = ?
            ORDER BY mr.score DESC
        """, (job_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        matches = []
        for row in rows:
            match_data = json.loads(row['match_data'])
            candidate_data = json.loads(row['candidate_data'])
            
            matches.append({
                'id': row['id'],
                'candidate_id': row['candidate_id'],
                'filename': row['filename'],
                'candidate_name': candidate_data.get('name', 'Unknown'),
                'score': row['score'],
                'justification': row['justification'],
                'match_details': match_data,
                'created_at': row['created_at']
            })
        
        return matches
    
    def clear_all_data(self):
        """
        Clear all data from all tables
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM match_results")
        cursor.execute("DELETE FROM job_postings")
        cursor.execute("DELETE FROM candidates")
        
        conn.commit()
        conn.close()
        
        print("✅ All data cleared from database")

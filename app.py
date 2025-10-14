"""
Smart Resume Screener - Main Application
Flask API for resume parsing, skill extraction, and job matching
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from pathlib import Path

from services.resume_parser import ResumeParser
from services.data_extractor import DataExtractor
from services.job_matcher import JobMatcher
from database.db_manager import DatabaseManager

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads/resumes'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

# Initialize services
db_manager = DatabaseManager()
resume_parser = ResumeParser()
data_extractor = DataExtractor()
job_matcher = JobMatcher()


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Smart Resume Screener API'
    }), 200


@app.route('/api/upload-resume', methods=['POST'])
def upload_resume():
    """
    Upload and parse a resume
    Returns: Structured candidate data with extracted information
    """
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Only PDF and TXT allowed'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Parse resume
        resume_text = resume_parser.parse(filepath)
        
        # Extract structured data using LLM
        candidate_data = data_extractor.extract_candidate_info(resume_text)
        
        # Save to database
        candidate_id = db_manager.save_candidate(filename, resume_text, candidate_data)
        
        return jsonify({
            'success': True,
            'candidate_id': candidate_id,
            'filename': filename,
            'data': candidate_data
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/match-job', methods=['POST'])
def match_job():
    """
    Match candidates against a job description
    Returns: List of candidates with match scores and justifications
    """
    try:
        data = request.get_json()
        
        if not data or 'job_description' not in data:
            return jsonify({'error': 'Job description is required'}), 400
        
        job_description = data['job_description']
        job_title = data.get('job_title', 'Position')
        threshold = data.get('threshold', 6.0)  # Minimum score threshold
        
        # Get all candidates from database
        candidates = db_manager.get_all_candidates()
        
        if not candidates:
            return jsonify({'error': 'No candidates found. Please upload resumes first.'}), 404
        
        # Match each candidate
        results = []
        for candidate in candidates:
            match_result = job_matcher.match_candidate(
                candidate['data'],
                candidate['resume_text'],
                job_description,
                job_title
            )
            
            if match_result['score'] >= threshold:
                results.append({
                    'candidate_id': candidate['id'],
                    'filename': candidate['filename'],
                    'name': candidate['data'].get('name', 'Unknown'),
                    'score': match_result['score'],
                    'justification': match_result['justification'],
                    'key_matches': match_result.get('key_matches', []),
                    'gaps': match_result.get('gaps', [])
                })
        
        # Sort by score (descending)
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Save job matching results
        job_id = db_manager.save_job_matching(job_title, job_description, results)
        
        return jsonify({
            'success': True,
            'job_id': job_id,
            'job_title': job_title,
            'threshold': threshold,
            'total_candidates': len(candidates),
            'shortlisted_count': len(results),
            'shortlisted_candidates': results
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    """Get all candidates"""
    try:
        candidates = db_manager.get_all_candidates()
        return jsonify({
            'success': True,
            'count': len(candidates),
            'candidates': candidates
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/candidate/<int:candidate_id>', methods=['GET'])
def get_candidate(candidate_id):
    """Get specific candidate details"""
    try:
        candidate = db_manager.get_candidate(candidate_id)
        if not candidate:
            return jsonify({'error': 'Candidate not found'}), 404
        
        return jsonify({
            'success': True,
            'candidate': candidate
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/job-history', methods=['GET'])
def get_job_history():
    """Get job matching history"""
    try:
        history = db_manager.get_job_history()
        return jsonify({
            'success': True,
            'count': len(history),
            'jobs': history
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Initialize database
    db_manager.init_db()
    
    # Run the application
    print("🚀 Starting Smart Resume Screener API...")
    print("📍 API available at: http://localhost:5000")
    print("✅ Health check: http://localhost:5000/health")
    app.run(debug=True, host='0.0.0.0', port=5000)

"""
Reset Database - Clear all data
"""
import sqlite3
from pathlib import Path
from config import Config

def reset_database():
    """Delete and recreate database"""
    db_path = Config.DATABASE_PATH
    
    # Delete database file if it exists
    if Path(db_path).exists():
        Path(db_path).unlink()
        print(f"✅ Deleted old database: {db_path}")
    
    # Recreate database
    from database.db_manager import DatabaseManager
    db = DatabaseManager()
    db.init_db()
    print("✅ Created fresh database")

if __name__ == "__main__":
    reset_database()

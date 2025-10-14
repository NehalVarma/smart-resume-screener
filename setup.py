"""
Quick Setup Script for Smart Resume Screener
This script helps you set up the application quickly
"""
import os
import sys
from pathlib import Path


def create_directory_structure():
    """Create necessary directories"""
    directories = [
        'uploads/resumes',
        'data',
        'samples/resumes',
        'samples/job_descriptions'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def check_env_file():
    """Check if .env file exists"""
    if not Path('.env').exists():
        print("\n⚠️  WARNING: .env file not found!")
        print("Please create a .env file with your OpenAI API key:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key")
        return False
    else:
        print("✓ .env file found")
        return True


def check_dependencies():
    """Check if dependencies are installed"""
    try:
        import flask
        import PyPDF2
        import pdfplumber
        import openai
        print("✓ All dependencies installed")
        return True
    except ImportError as e:
        print(f"\n⚠️  Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False


def initialize_database():
    """Initialize the database"""
    try:
        from database.db_manager import DatabaseManager
        db = DatabaseManager()
        db.init_db()
        print("✓ Database initialized")
        return True
    except Exception as e:
        print(f"⚠️  Error initializing database: {e}")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("🎯 Smart Resume Screener - Setup")
    print("=" * 60)
    print()
    
    print("Step 1: Creating directory structure...")
    create_directory_structure()
    print()
    
    print("Step 2: Checking environment file...")
    env_ok = check_env_file()
    print()
    
    print("Step 3: Checking dependencies...")
    deps_ok = check_dependencies()
    print()
    
    if env_ok and deps_ok:
        print("Step 4: Initializing database...")
        db_ok = initialize_database()
        print()
    else:
        db_ok = False
    
    print("=" * 60)
    if env_ok and deps_ok and db_ok:
        print("✅ Setup complete!")
        print()
        print("Next steps:")
        print("1. Run the backend: python app.py")
        print("2. Open frontend/index.html in your browser")
        print("3. Upload resumes and start matching!")
    else:
        print("❌ Setup incomplete. Please fix the issues above.")
    print("=" * 60)


if __name__ == "__main__":
    main()

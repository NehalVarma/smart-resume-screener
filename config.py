"""
Configuration settings for Smart Resume Screener
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # Database Configuration
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'data/resumes.db')
    
    # File Upload Configuration
    UPLOAD_FOLDER = 'uploads/resumes'
    MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'pdf', 'txt'}
    
    # Matching Configuration
    DEFAULT_MATCH_THRESHOLD = 6.0  # Minimum score for shortlisting
    
    @staticmethod
    def validate():
        """Validate critical configuration"""
        if not Config.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please set it in .env file"
            )

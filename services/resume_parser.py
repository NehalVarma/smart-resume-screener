"""
Resume Parser Service
Extracts text from PDF and TXT files
"""
import PyPDF2
import pdfplumber
from pathlib import Path


class ResumeParser:
    """Parse resumes from PDF and text files"""
    
    def parse(self, filepath):
        """
        Parse resume file and extract text
        
        Args:
            filepath: Path to resume file (PDF or TXT)
            
        Returns:
            Extracted text from resume
        """
        file_extension = Path(filepath).suffix.lower()
        
        if file_extension == '.pdf':
            return self._parse_pdf(filepath)
        elif file_extension == '.txt':
            return self._parse_txt(filepath)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
    
    def _parse_pdf(self, filepath):
        """
        Extract text from PDF using pdfplumber (primary) with PyPDF2 fallback
        
        Args:
            filepath: Path to PDF file
            
        Returns:
            Extracted text
        """
        try:
            # Try pdfplumber first (better for complex layouts)
            with pdfplumber.open(filepath) as pdf:
                text_parts = []
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        text_parts.append(text)
                
                if text_parts:
                    return '\n\n'.join(text_parts)
            
            # Fallback to PyPDF2 if pdfplumber fails
            return self._parse_pdf_pypdf2(filepath)
            
        except Exception as e:
            print(f"Error parsing PDF with pdfplumber: {e}")
            # Try PyPDF2 as fallback
            return self._parse_pdf_pypdf2(filepath)
    
    def _parse_pdf_pypdf2(self, filepath):
        """
        Fallback PDF parser using PyPDF2
        
        Args:
            filepath: Path to PDF file
            
        Returns:
            Extracted text
        """
        try:
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text_parts = []
                
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        text_parts.append(text)
                
                return '\n\n'.join(text_parts)
                
        except Exception as e:
            raise Exception(f"Failed to parse PDF: {str(e)}")
    
    def _parse_txt(self, filepath):
        """
        Extract text from TXT file
        
        Args:
            filepath: Path to text file
            
        Returns:
            File contents
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Try different encoding
            with open(filepath, 'r', encoding='latin-1') as file:
                return file.read()

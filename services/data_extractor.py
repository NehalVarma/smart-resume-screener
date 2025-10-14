"""
Data Extractor Service
Uses LLM to extract structured data from resume text
"""
import json
import openai
from config import Config


class DataExtractor:
    """Extract structured candidate information using LLM"""
    
    def __init__(self):
        """Initialize with OpenAI configuration"""
        Config.validate()
        openai.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL
    
    def extract_candidate_info(self, resume_text):
        """
        Extract structured information from resume text using LLM
        
        Args:
            resume_text: Raw text extracted from resume
            
        Returns:
            Dictionary with structured candidate information
        """
        prompt = self._build_extraction_prompt(resume_text)
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert HR assistant that extracts structured information from resumes. Always respond with valid JSON only."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            extracted_data = json.loads(response.choices[0].message.content)
            return self._validate_and_format(extracted_data)
            
        except Exception as e:
            print(f"Error extracting data with LLM: {e}")
            # Return minimal structure on error
            return self._get_fallback_structure()
    
    def _build_extraction_prompt(self, resume_text):
        """
        Build the extraction prompt for the LLM
        
        Args:
            resume_text: Resume text to analyze
            
        Returns:
            Formatted prompt string
        """
        return f"""
Extract structured information from the following resume and return it as a JSON object with this exact structure:

{{
  "name": "Full name of the candidate",
  "email": "Email address",
  "phone": "Phone number",
  "location": "Location/City",
  "summary": "Brief professional summary (2-3 sentences)",
  "skills": [
    "List of technical and professional skills"
  ],
  "experience": [
    {{
      "title": "Job title",
      "company": "Company name",
      "duration": "Time period (e.g., Jan 2020 - Present)",
      "description": "Brief description of role and achievements"
    }}
  ],
  "education": [
    {{
      "degree": "Degree name",
      "institution": "University/School name",
      "year": "Graduation year or period",
      "field": "Field of study"
    }}
  ],
  "certifications": [
    "List of certifications, if any"
  ],
  "languages": [
    "List of languages spoken"
  ],
  "total_experience_years": "Estimated total years of experience as a number"
}}

IMPORTANT:
- Extract only information that is explicitly present in the resume
- Use "Not specified" for missing information
- Keep descriptions concise
- For skills, include both technical skills (programming languages, tools) and soft skills
- Return ONLY valid JSON, no additional text

Resume Text:
{resume_text}
"""
    
    def _validate_and_format(self, data):
        """
        Validate and format extracted data
        
        Args:
            data: Raw extracted data
            
        Returns:
            Validated and formatted data
        """
        # Ensure required fields exist
        required_fields = ['name', 'skills', 'experience', 'education']
        for field in required_fields:
            if field not in data:
                data[field] = [] if field in ['skills', 'experience', 'education'] else "Not specified"
        
        # Ensure arrays are arrays
        if not isinstance(data.get('skills', []), list):
            data['skills'] = []
        if not isinstance(data.get('experience', []), list):
            data['experience'] = []
        if not isinstance(data.get('education', []), list):
            data['education'] = []
        if not isinstance(data.get('certifications', []), list):
            data['certifications'] = []
        
        return data
    
    def _get_fallback_structure(self):
        """
        Return minimal data structure when extraction fails
        
        Returns:
            Minimal valid structure
        """
        return {
            "name": "Unknown",
            "email": "Not specified",
            "phone": "Not specified",
            "location": "Not specified",
            "summary": "Could not extract information",
            "skills": [],
            "experience": [],
            "education": [],
            "certifications": [],
            "languages": [],
            "total_experience_years": 0
        }

"""
Job Matcher Service
Uses LLM to match candidates with job descriptions and provide scoring
"""
import json
import openai
from config import Config


class JobMatcher:
    """Match candidates with job descriptions using semantic analysis"""
    
    def __init__(self):
        """Initialize with OpenAI configuration"""
        Config.validate()
        openai.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL
    
    def match_candidate(self, candidate_data, resume_text, job_description, job_title):
        """
        Match a candidate against a job description
        
        Args:
            candidate_data: Structured candidate information
            resume_text: Full resume text
            job_description: Job description text
            job_title: Title of the position
            
        Returns:
            Dictionary with match score, justification, and detailed analysis
        """
        prompt = self._build_matching_prompt(
            candidate_data,
            resume_text,
            job_description,
            job_title
        )
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert HR recruiter and talent matcher. 
                        Your task is to objectively evaluate how well a candidate matches a job description.
                        Provide honest assessments with specific evidence from the resume.
                        Always respond with valid JSON only."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.5,
                response_format={"type": "json_object"}
            )
            
            match_result = json.loads(response.choices[0].message.content)
            return self._validate_match_result(match_result)
            
        except Exception as e:
            print(f"Error matching candidate: {e}")
            return self._get_fallback_match_result()
    
    def _build_matching_prompt(self, candidate_data, resume_text, job_description, job_title):
        """
        Build the matching prompt for the LLM
        
        Args:
            candidate_data: Structured candidate data
            resume_text: Full resume text
            job_description: Job description
            job_title: Job title
            
        Returns:
            Formatted prompt string
        """
        return f"""
Compare the following candidate with the job description and provide a comprehensive match analysis.

JOB TITLE: {job_title}

JOB DESCRIPTION:
{job_description}

CANDIDATE PROFILE:
Name: {candidate_data.get('name', 'Unknown')}
Skills: {', '.join(candidate_data.get('skills', []))}
Experience: {candidate_data.get('total_experience_years', 'Unknown')} years
Summary: {candidate_data.get('summary', 'Not provided')}

FULL RESUME TEXT:
{resume_text[:3000]}  # Limit to first 3000 chars to manage token usage

YOUR TASK:
Analyze the candidate's fit for this role and return a JSON object with this exact structure:

{{
  "score": 7.5,
  "justification": "A detailed 2-3 paragraph explanation of why this score was given, covering strengths and weaknesses",
  "key_matches": [
    "Specific skill/experience match 1",
    "Specific skill/experience match 2",
    "Specific skill/experience match 3"
  ],
  "gaps": [
    "Missing skill or experience 1",
    "Missing skill or experience 2"
  ],
  "strengths": [
    "Key strength 1",
    "Key strength 2",
    "Key strength 3"
  ],
  "recommendation": "STRONG_FIT | GOOD_FIT | MODERATE_FIT | WEAK_FIT"
}}

SCORING CRITERIA (1-10 scale):
- 9-10: Exceptional fit - All key requirements met, strong relevant experience
- 7-8: Strong fit - Most requirements met, good relevant experience
- 5-6: Moderate fit - Some requirements met, partial relevant experience
- 3-4: Weak fit - Few requirements met, limited relevant experience
- 1-2: Poor fit - Very few or no requirements met

Be specific and reference actual skills, experiences, and qualifications from the resume.
Consider: technical skills, years of experience, relevant domain knowledge, education, and cultural indicators.
Return ONLY valid JSON, no additional text.
"""
    
    def _validate_match_result(self, result):
        """
        Validate and format match result
        
        Args:
            result: Raw match result from LLM
            
        Returns:
            Validated match result
        """
        # Ensure score is a number between 0 and 10
        try:
            score = float(result.get('score', 0))
            result['score'] = max(0.0, min(10.0, score))
        except (ValueError, TypeError):
            result['score'] = 0.0
        
        # Ensure required fields exist
        if 'justification' not in result or not result['justification']:
            result['justification'] = "No justification provided"
        
        if 'key_matches' not in result or not isinstance(result['key_matches'], list):
            result['key_matches'] = []
        
        if 'gaps' not in result or not isinstance(result['gaps'], list):
            result['gaps'] = []
        
        if 'strengths' not in result or not isinstance(result['strengths'], list):
            result['strengths'] = []
        
        if 'recommendation' not in result:
            # Derive recommendation from score
            score = result['score']
            if score >= 8:
                result['recommendation'] = "STRONG_FIT"
            elif score >= 6:
                result['recommendation'] = "GOOD_FIT"
            elif score >= 4:
                result['recommendation'] = "MODERATE_FIT"
            else:
                result['recommendation'] = "WEAK_FIT"
        
        return result
    
    def _get_fallback_match_result(self):
        """
        Return minimal match result when matching fails
        
        Returns:
            Minimal valid match result
        """
        return {
            "score": 0.0,
            "justification": "Unable to perform matching analysis",
            "key_matches": [],
            "gaps": [],
            "strengths": [],
            "recommendation": "UNKNOWN"
        }

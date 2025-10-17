"""
Mock Data Extractor Service (for demo without OpenAI credits)
Simulates LLM extraction without actual API calls
"""
import json


class DataExtractor:
    """Extract structured candidate information using mock data"""
    
    def __init__(self):
        """Initialize without OpenAI"""
        pass
    
    def extract_candidate_info(self, resume_text):
        """
        Extract structured information from resume text using pattern matching
        
        Args:
            resume_text: Raw text extracted from resume
            
        Returns:
            Dictionary with structured candidate information
        """
        # Extract name (first line or NAME header)
        lines = resume_text.strip().split('\n')
        name = lines[0].strip() if lines else "Unknown Candidate"
        
        # Extract email
        import re
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)
        email = email_match.group(0) if email_match else "Not specified"
        
        # Extract phone
        phone_match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', resume_text)
        phone = phone_match.group(0) if phone_match else "Not specified"
        
        # Extract skills (common technical keywords)
        skills_keywords = [
            'Python', 'JavaScript', 'Java', 'C++', 'React', 'Angular', 'Vue', 'Node.js',
            'Django', 'Flask', 'FastAPI', 'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP',
            'SQL', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Git', 'CI/CD', 'Jenkins',
            'TensorFlow', 'PyTorch', 'Machine Learning', 'Deep Learning', 'NLP', 'scikit-learn',
            'Pandas', 'NumPy', 'HTML', 'CSS', 'TypeScript', 'GraphQL', 'REST', 'Microservices',
            'Terraform', 'Ansible', 'Linux', 'Bash', 'API', 'Agile', 'Scrum'
        ]
        
        skills = []
        resume_lower = resume_text.lower()
        for skill in skills_keywords:
            if skill.lower() in resume_lower:
                skills.append(skill)
        
        # Extract experience years
        exp_match = re.search(r'(\d+)\+?\s*years?\s*(of)?\s*(experience|exp)', resume_text, re.IGNORECASE)
        total_exp = int(exp_match.group(1)) if exp_match else 0
        
        # Build experience section
        experience = []
        if 'senior' in resume_lower or 'lead' in resume_lower or total_exp >= 5:
            experience.append({
                "title": "Senior Engineer" if total_exp >= 5 else "Engineer",
                "company": "Tech Company",
                "duration": f"{total_exp} years",
                "description": "Developed software solutions and led projects"
            })
        elif 'engineer' in resume_lower or 'developer' in resume_lower:
            experience.append({
                "title": "Software Engineer",
                "company": "Technology Firm",
                "duration": f"{total_exp} years",
                "description": "Built and maintained software applications"
            })
        
        # Build education section
        education = []
        if 'bachelor' in resume_lower or 'b.s.' in resume_lower or 'bs' in resume_lower:
            education.append({
                "degree": "Bachelor of Science",
                "institution": "University",
                "year": "2017",
                "field": "Computer Science"
            })
        if 'master' in resume_lower or 'm.s.' in resume_lower:
            education.append({
                "degree": "Master of Science",
                "institution": "University",
                "year": "2019",
                "field": "Computer Science"
            })
        
        # Create summary
        summary = f"Professional with {total_exp}+ years of experience in software development."
        if skills:
            summary += f" Skilled in {', '.join(skills[:3])}."
        
        return {
            "name": name,
            "email": email,
            "phone": phone,
            "location": "Not specified",
            "summary": summary,
            "skills": skills[:15],  # Top 15 skills
            "experience": experience if experience else [{
                "title": "Professional",
                "company": "Various Companies",
                "duration": f"{total_exp} years",
                "description": "Software development experience"
            }],
            "education": education if education else [{
                "degree": "Bachelor's Degree",
                "institution": "University",
                "year": "Not specified",
                "field": "Computer Science"
            }],
            "certifications": [],
            "languages": ["English"],
            "total_experience_years": total_exp
        }

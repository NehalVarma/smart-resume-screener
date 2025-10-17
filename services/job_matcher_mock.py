"""
Mock Job Matcher Service (for demo without OpenAI credits)
Simulates LLM matching without actual API calls
"""
import json


class JobMatcher:
    """Match candidates with job descriptions using keyword matching"""
    
    def __init__(self):
        """Initialize without OpenAI"""
        pass
    
    def match_candidate(self, candidate_data, resume_text, job_description, job_title):
        """
        Match a candidate against a job description using keyword analysis
        
        Args:
            candidate_data: Structured candidate information
            resume_text: Full resume text
            job_description: Job description text
            job_title: Title of the position
            
        Returns:
            Dictionary with match score, justification, and detailed analysis
        """
        # Extract job requirements
        job_lower = job_description.lower()
        resume_lower = resume_text.lower()
        
        # Common technical skills to check
        required_skills = []
        preferred_skills = []
        
        # Identify job type
        is_fullstack = any(word in job_lower for word in ['full stack', 'fullstack', 'full-stack'])
        is_devops = any(word in job_lower for word in ['devops', 'sre', 'site reliability'])
        is_data_science = any(word in job_lower for word in ['data scient', 'machine learning', 'ml engineer'])
        
        # Define skill sets for different roles
        if is_fullstack:
            required_skills = ['python', 'javascript', 'react', 'node', 'api', 'database']
            preferred_skills = ['docker', 'aws', 'typescript', 'mongodb']
        elif is_devops:
            required_skills = ['aws', 'docker', 'kubernetes', 'terraform', 'ci/cd', 'linux']
            preferred_skills = ['ansible', 'prometheus', 'jenkins', 'python']
        elif is_data_science:
            required_skills = ['python', 'machine learning', 'tensorflow', 'pytorch', 'pandas', 'numpy']
            preferred_skills = ['nlp', 'deep learning', 'spark', 'sql']
        else:
            # Generic software role
            required_skills = ['programming', 'software', 'development', 'git']
            preferred_skills = ['cloud', 'database', 'api']
        
        # Calculate match score (much stricter)
        required_matches = sum(1 for skill in required_skills if skill in resume_lower)
        preferred_matches = sum(1 for skill in preferred_skills if skill in resume_lower)
        
        # Strict scoring: need most required skills to get high score
        required_percentage = required_matches / len(required_skills) if required_skills else 0
        preferred_percentage = preferred_matches / len(preferred_skills) if preferred_skills else 0
        
        # Base score heavily weighted on required skills
        required_score = required_percentage * 6.5  # Max 6.5 from required
        preferred_score = preferred_percentage * 2.0  # Max 2.0 from preferred
        
        base_score = required_score + preferred_score
        
        # Experience adjustment (stricter)
        exp_years = candidate_data.get('total_experience_years', 0)
        if '5+' in job_lower or 'senior' in job_lower:
            if exp_years >= 5:
                base_score += 0.8
            elif exp_years >= 3:
                base_score += 0.3
            else:
                base_score -= 1.5  # Heavy penalty for junior on senior role
        
        # Penalize if very few matches
        if required_percentage < 0.4:
            base_score *= 0.7  # Reduce score by 30% if less than 40% match
        
        # Cap score between 1 and 10, but more realistic distribution
        final_score = min(9.5, max(1.0, base_score))
        
        # Round to one decimal to look more realistic
        final_score = round(final_score, 1)
        
        # Generate justification
        candidate_name = candidate_data.get('name', 'The candidate')
        candidate_skills = candidate_data.get('skills', [])
        
        # Find matching skills
        key_matches = []
        for skill in candidate_skills:
            if skill.lower() in job_lower:
                key_matches.append(f"Has {skill} experience")
        
        # Find missing skills
        gaps = []
        for skill in required_skills:
            if skill not in resume_lower:
                gaps.append(f"Limited {skill.capitalize()} experience mentioned")
        
        # Generate justification based on score
        if final_score >= 8:
            justification = f"{candidate_name} is a strong match for the {job_title} position. "
            justification += f"With {exp_years}+ years of experience, they demonstrate proficiency in key required technologies. "
            justification += f"Their background in {', '.join(candidate_skills[:3])} aligns well with the job requirements. "
            if key_matches:
                justification += "The candidate's expertise in the core technologies mentioned in the job description makes them a highly qualified candidate. "
            justification += "This candidate should be prioritized for interviews."
        elif final_score >= 6:
            justification = f"{candidate_name} shows good potential for the {job_title} role. "
            justification += f"They have {exp_years} years of relevant experience and possess several of the required skills. "
            if key_matches:
                justification += f"Notably, they have experience with {len(key_matches)} key technologies mentioned in the job posting. "
            if gaps:
                justification += f"However, some skills like {gaps[0].split('Limited ')[1] if gaps else 'certain technologies'} could be developed further. "
            justification += "Overall, this is a solid candidate worth considering."
        elif final_score >= 4:
            justification = f"{candidate_name} has moderate alignment with the {job_title} position. "
            justification += f"While they bring {exp_years} years of experience, there are notable gaps in the required skill set. "
            if key_matches:
                justification += f"They do have some relevant experience, particularly in {len(key_matches)} areas. "
            justification += "Additional training or mentoring might be needed. Consider as a backup candidate."
        else:
            justification = f"{candidate_name}'s profile shows limited alignment with the {job_title} requirements. "
            justification += "Their background and skill set appear to be focused in a different technical domain. "
            if gaps:
                justification += f"Key gaps include {len(gaps)} critical skills mentioned in the job description. "
            justification += "This candidate may not be the best fit for this particular role."
        
        # Determine recommendation
        if final_score >= 8:
            recommendation = "STRONG_FIT"
        elif final_score >= 6:
            recommendation = "GOOD_FIT"
        elif final_score >= 4:
            recommendation = "MODERATE_FIT"
        else:
            recommendation = "WEAK_FIT"
        
        # Generate strengths
        strengths = []
        if exp_years >= 5:
            strengths.append(f"Extensive experience ({exp_years}+ years)")
        if len(candidate_skills) > 10:
            strengths.append("Diverse technical skill set")
        if required_matches > len(required_skills) * 0.6:
            strengths.append("Strong match with core requirements")
        if not strengths:
            strengths = ["Has relevant industry experience"]
        
        return {
            "score": round(final_score, 1),
            "justification": justification,
            "key_matches": key_matches[:5] if key_matches else ["Some transferable skills"],
            "gaps": gaps[:3] if gaps else [],
            "strengths": strengths,
            "recommendation": recommendation
        }

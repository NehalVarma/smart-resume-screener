# Smart Resume Screener - Demo Script

## 🎥 Video Recording Guide (2-3 minutes)

### Before Recording
- [ ] Start the Flask backend server
- [ ] Open the frontend in browser
- [ ] Have sample resumes ready
- [ ] Prepare a job description
- [ ] Test the complete flow once

---

## 📝 Demo Script

### **INTRO (15 seconds)**

**Script:**
> "Hi! I'm demonstrating the Smart Resume Screener - an AI-powered application that intelligently parses resumes and matches candidates with job descriptions. Let's see it in action!"

**Actions:**
- Show the application landing page
- Quick overview of the interface

---

### **SECTION 1: Upload Resumes (40 seconds)**

**Script:**
> "First, I'll upload three sample resumes. The system supports both PDF and text formats."

**Actions:**
1. Click "Choose Files" button
2. Select all 3 sample resumes:
   - `john_doe_software_engineer.txt`
   - `sarah_chen_data_scientist.txt`
   - `michael_rodriguez_devops.txt`
3. Click "Upload Resumes"
4. Show the upload status messages
5. Point out the extracted candidate names appearing

**Key Points to Mention:**
- "The application uses AI to extract structured information like skills, experience, and education from each resume"
- "Notice how it identifies the candidate names automatically"

---

### **SECTION 2: Enter Job Description (20 seconds)**

**Script:**
> "Now I'll enter a job description. Let's say we're looking for a Senior Full Stack Engineer."

**Actions:**
1. Type in Job Title: "Senior Full Stack Engineer"
2. Paste the job description from `samples/job_descriptions/senior_fullstack_engineer.txt`
3. Show the threshold setting (keep at 6.0)

**Key Points:**
- "The threshold determines the minimum match score for shortlisting"
- "I'll keep it at 6 out of 10"

---

### **SECTION 3: Match Candidates (50 seconds)**

**Script:**
> "Let's find the best matches. The system uses semantic analysis to compare each candidate's skills and experience with the job requirements."

**Actions:**
1. Click "Find Best Matches"
2. Show the processing indicator
3. Wait for results to load (~5-10 seconds)
4. Scroll through the results

**Key Points to Highlight:**
- "Here are the results ranked by match score"
- Point to the top candidate's score (likely John Doe with ~8-9/10)
- Read a snippet of the justification
- Show the "Key Matches" section - highlight specific skills
- Show the "Gaps" section - point out missing requirements

**Example narration:**
> "Our top match is John Doe with a score of 8.5 out of 10. The system identified that he has strong experience in Python, React, and cloud technologies - all required for this role. However, it also noted some gaps like limited GraphQL experience."

---

### **SECTION 4: Additional Candidate (20 seconds)**

**Script:**
> "Let's look at another candidate."

**Actions:**
1. Scroll to the second candidate (likely Sarah Chen)
2. Show their score (might be lower like 5-6/10)
3. Briefly explain the justification

**Key Points:**
> "Sarah is an excellent Data Scientist but scored lower because her expertise is more focused on machine learning than full-stack web development. The AI identified this mismatch."

---

### **SECTION 5: Architecture & LLM Prompts (15 seconds)**

**Script:**
> "Behind the scenes, this application uses a Flask backend with OpenAI's GPT model for intelligent parsing and matching."

**Actions:**
1. Quickly switch to VS Code or show architecture diagram
2. Show the README file
3. Point to the LLM prompts section

**Key Points:**
- "The prompts are carefully designed to extract structured data and provide objective scoring"
- "All match results and candidate data are stored in a SQLite database"

---

### **OUTRO (10 seconds)**

**Script:**
> "This demonstrates how AI can streamline the resume screening process, providing objective scores with clear justifications. The complete code, documentation, and setup instructions are available in the GitHub repository. Thank you!"

**Actions:**
- Show the GitHub repo structure briefly
- End on the README or application screen

---

## 🎬 Recording Tips

### Technical Setup
1. **Screen Resolution:** Use 1920x1080 for best quality
2. **Recording Tool:** Use OBS Studio, Loom, or QuickTime
3. **Audio:** Use a good microphone, speak clearly
4. **Browser:** Use full-screen mode (F11) for cleaner look

### Best Practices
- **Practice First:** Run through the demo 2-3 times before recording
- **Pace Yourself:** Don't rush, speak naturally
- **Highlight Key Features:** Focus on AI capabilities and user experience
- **Show Results Clearly:** Let the scores and justifications be visible
- **Keep Time:** Aim for 2-3 minutes total

### Common Issues to Avoid
- ❌ API errors (ensure backend is running)
- ❌ Slow processing (test API response times first)
- ❌ Missing files (verify all sample data exists)
- ❌ Speaking too fast
- ❌ Not showing enough of the results

---

## 📋 Pre-Recording Checklist

### Backend
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with OpenAI API key
- [ ] Flask server running (`python app.py`)
- [ ] Health check passes: http://localhost:5000/health

### Frontend
- [ ] `frontend/index.html` opens in browser
- [ ] No console errors
- [ ] Can connect to backend API

### Sample Data
- [ ] 3 resume files in `samples/resumes/`
- [ ] 3 job descriptions in `samples/job_descriptions/`
- [ ] Files are readable

### Test Run
- [ ] Upload one resume successfully
- [ ] Extract data works
- [ ] Job matching returns results
- [ ] Scores and justifications display properly

---

## 🎯 Key Messages to Convey

1. **Problem Solved:** "Manual resume screening is time-consuming and subjective"

2. **Solution:** "AI-powered semantic matching provides objective, fast screening"

3. **Value:** 
   - Saves time for recruiters
   - Reduces bias through objective scoring
   - Provides clear justifications for decisions

4. **Technical Excellence:**
   - Clean code structure
   - RESTful API design
   - LLM integration
   - Full-stack application

5. **Deliverables:**
   - Complete working application
   - Comprehensive documentation
   - Sample data
   - Ready for deployment

---

## 📊 Alternative Demo Scenarios

### Scenario A: Perfect Match
- Use John Doe's resume
- Match with "Senior Full Stack Engineer" job
- Expected: High score (8-9/10)

### Scenario B: Partial Match
- Use Sarah Chen's resume
- Match with "Senior Full Stack Engineer" job
- Expected: Lower score (5-6/10), shows skills mismatch

### Scenario C: Excellent Match
- Use Michael Rodriguez's resume
- Match with "DevOps Engineer" job description
- Expected: Very high score (9+/10)

---

## 🔍 What Evaluators Look For

Based on the evaluation criteria, emphasize:

1. **Code Quality & Structure**
   - Show organized folder structure
   - Mention separation of concerns (services, database, API)

2. **Data Extraction**
   - Highlight the structured JSON output
   - Show skills, experience, education extraction

3. **LLM Prompt Quality**
   - Briefly show or mention the detailed prompts
   - Explain scoring criteria (1-10 scale with justifications)

4. **Output Clarity**
   - Demonstrate clear UI
   - Show readable justifications
   - Highlight key matches and gaps

---

## 💡 Talking Points

### Why This Solution Works
- "Uses state-of-the-art LLM for semantic understanding"
- "Goes beyond keyword matching to understand context"
- "Provides transparency with detailed justifications"
- "Scalable architecture ready for production"

### Technical Highlights
- "RESTful API design following best practices"
- "Modular code structure for maintainability"
- "Database storage for historical analysis"
- "Responsive web interface"

### Future Enhancements (if asked)
- "Could add support for more file formats"
- "Integrate with ATS systems"
- "Add batch processing for large volumes"
- "Implement advanced analytics dashboard"

---

## 📹 Recommended Recording Flow

**Total Time: 2:30 - 3:00 minutes**

| Section | Time | Focus |
|---------|------|-------|
| Intro | 0:00-0:15 | Problem & Solution |
| Upload Resumes | 0:15-0:55 | Data extraction demo |
| Job Description | 0:55-1:15 | Setup matching |
| View Results | 1:15-2:05 | AI matching analysis |
| Architecture | 2:05-2:20 | Technical overview |
| Outro | 2:20-2:30 | Summary & CTA |

---

**Good luck with your demo! 🚀**

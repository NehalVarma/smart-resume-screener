# 🎯 Smart Resume Screener

An intelligent resume screening application that uses Large Language Models (LLMs) to parse resumes, extract structured information, and match candidates with job descriptions.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [LLM Prompts](#llm-prompts)
- [Demo](#demo)
- [Project Structure](#project-structure)

## 🎥 Overview

The Smart Resume Screener is a full-stack application that automates the resume screening process using AI. It intelligently parses resumes (PDF/TXT), extracts structured data (skills, experience, education), and uses semantic matching to score candidates against job descriptions.

### Key Benefits:
- **Time Saving**: Automate initial resume screening
- **Objective Analysis**: AI-powered semantic matching reduces bias
- **Structured Data**: Extract and store candidate information in a structured format
- **Transparent Scoring**: Get detailed justifications for each match score

## ✨ Features

- 📄 **Multi-format Support**: Upload PDF and TXT resumes
- 🤖 **AI-Powered Extraction**: Extract skills, experience, education using LLM
- 🎯 **Semantic Matching**: Compare candidates with job descriptions using semantic analysis
- 📊 **Scoring System**: Get match scores (1-10) with detailed justifications
- 💾 **Database Storage**: Store parsed resumes and match results
- 🌐 **Web Dashboard**: User-friendly interface for uploading and viewing results
- 📈 **Detailed Analysis**: View key matches, gaps, and strengths for each candidate
- 🔍 **Configurable Threshold**: Filter candidates by minimum match score

## 🏗️ Architecture

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│   Frontend  │  HTTP    │   Flask API  │          │   OpenAI    │
│  (HTML/JS)  │ ────────>│   Backend    │ ────────>│  LLM API    │
└─────────────┘          └──────────────┘          └─────────────┘
                                │
                                │
                         ┌──────▼───────┐
                         │   SQLite     │
                         │   Database   │
                         └──────────────┘
```

### Data Flow:

1. **Upload**: User uploads resume (PDF/TXT) via frontend
2. **Parse**: Backend extracts text from the file
3. **Extract**: LLM extracts structured data (skills, experience, education)
4. **Store**: Data saved to SQLite database
5. **Match**: When job description is submitted, LLM compares each candidate
6. **Score**: Each candidate receives a 1-10 score with justification
7. **Display**: Results shown in frontend, sorted by score

## 🛠️ Technology Stack

### Backend:
- **Python 3.8+**
- **Flask**: Web framework
- **PyPDF2/pdfplumber**: PDF text extraction
- **OpenAI API**: LLM for data extraction and matching
- **SQLite**: Database for storing resumes and results

### Frontend:
- **HTML5/CSS3**: Structure and styling
- **Vanilla JavaScript**: Frontend logic
- **Fetch API**: HTTP requests to backend

### Database Schema:

```sql
-- Candidates table
candidates (
    id, filename, resume_text, data (JSON), created_at
)

-- Job postings table
job_postings (
    id, job_title, job_description, created_at
)

-- Match results table
match_results (
    id, job_id, candidate_id, score, justification, match_data (JSON), created_at
)
```

## 📥 Installation

### Prerequisites:
- Python 3.8 or higher
- OpenAI API key

### Step 1: Clone the Repository

```bash
cd c:\Users\nehal\Desktop\HPE\smart-resume-screener
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
DATABASE_PATH=data/resumes.db
```

## ⚙️ Configuration

### OpenAI API Key

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add it to the `.env` file
3. Ensure you have credits in your OpenAI account

### Model Selection

The application uses `gpt-3.5-turbo` by default. You can change to `gpt-4` for better results:

```
OPENAI_MODEL=gpt-4
```

**Note**: GPT-4 is more expensive but provides better analysis.

## 🚀 Usage

### Start the Backend Server

```bash
python app.py
```

The API will start at: `http://localhost:5000`

### Open the Frontend

Open `frontend/index.html` in your web browser, or serve it:

```bash
cd frontend
python -m http.server 8000
```

Then navigate to: `http://localhost:8000`

### Using the Application

1. **Upload Resumes**:
   - Click "Choose Files" and select PDF or TXT resumes
   - Click "Upload Resumes"
   - Wait for confirmation

2. **Enter Job Description**:
   - Enter the job title
   - Paste the job description
   - Set minimum match threshold (default: 6.0)

3. **Find Matches**:
   - Click "Find Best Matches"
   - View shortlisted candidates with scores and justifications

## 📡 API Endpoints

### Health Check
```
GET /health
```
Returns API status.

### Upload Resume
```
POST /api/upload-resume
Content-Type: multipart/form-data

Body: file (PDF or TXT)
```

**Response:**
```json
{
  "success": true,
  "candidate_id": 1,
  "filename": "john_doe.pdf",
  "data": {
    "name": "John Doe",
    "skills": ["Python", "Machine Learning", "Docker"],
    "experience": [...],
    "education": [...]
  }
}
```

### Match Candidates with Job
```
POST /api/match-job
Content-Type: application/json

Body:
{
  "job_title": "Senior Software Engineer",
  "job_description": "We are looking for...",
  "threshold": 6.0
}
```

**Response:**
```json
{
  "success": true,
  "job_id": 1,
  "total_candidates": 10,
  "shortlisted_count": 5,
  "shortlisted_candidates": [
    {
      "candidate_id": 1,
      "name": "John Doe",
      "score": 8.5,
      "justification": "Strong match because...",
      "key_matches": ["Python expert", "5 years ML experience"],
      "gaps": ["No cloud experience mentioned"]
    }
  ]
}
```

### Get All Candidates
```
GET /api/candidates
```

### Get Candidate Details
```
GET /api/candidate/<id>
```

### Get Job History
```
GET /api/job-history
```

## 🤖 LLM Prompts

### Data Extraction Prompt

The application uses a structured prompt to extract candidate information:

```
Extract structured information from the following resume and return it as a JSON object with this exact structure:

{
  "name": "Full name of the candidate",
  "email": "Email address",
  "phone": "Phone number",
  "location": "Location/City",
  "summary": "Brief professional summary",
  "skills": ["List of skills"],
  "experience": [
    {
      "title": "Job title",
      "company": "Company name",
      "duration": "Time period",
      "description": "Brief description"
    }
  ],
  "education": [...],
  "certifications": [...],
  "total_experience_years": 5
}

Resume Text:
[RESUME_TEXT]
```

### Job Matching Prompt

For semantic matching and scoring:

```
Compare the following candidate with the job description and provide a comprehensive match analysis.

JOB TITLE: [JOB_TITLE]
JOB DESCRIPTION: [JOB_DESCRIPTION]

CANDIDATE PROFILE:
Name: [NAME]
Skills: [SKILLS]
Experience: [YEARS] years

YOUR TASK:
Analyze the candidate's fit for this role and return a JSON object with:

{
  "score": 7.5,
  "justification": "Detailed explanation...",
  "key_matches": ["Match 1", "Match 2"],
  "gaps": ["Gap 1", "Gap 2"],
  "strengths": ["Strength 1", "Strength 2"],
  "recommendation": "STRONG_FIT | GOOD_FIT | MODERATE_FIT | WEAK_FIT"
}

SCORING CRITERIA (1-10):
- 9-10: Exceptional fit
- 7-8: Strong fit
- 5-6: Moderate fit
- 3-4: Weak fit
- 1-2: Poor fit
```

## 🎬 Demo Video

### 📺 Watch the Complete Demonstration

> 2-3 minute walkthrough of the Smart Resume Screener in action

<!-- 
🎥 TO ADD YOUR VIDEO:
1. Go to GitHub: https://github.com/NehalVarma/smart-resume-screener
2. Click on README.md and then the ✏️ Edit button
3. Come to this section
4. DRAG AND DROP your video file (.mp4) here in the editor
5. GitHub will upload it and generate a URL like: https://github.com/user-attachments/assets/[id]/video.mp4
6. The video will play directly in the README!
-->

**What you'll see in the demo:**
- ✅ **Resume Upload**: Uploading multiple resumes (PDF/TXT format)
- ✅ **AI Parsing**: Real-time data extraction using LLM
- ✅ **Job Matching**: Semantic analysis comparing candidates with job requirements  
- ✅ **Results Display**: Match scores (1-10), detailed justifications, and key insights
- ✅ **Code Walkthrough**: Architecture overview and implementation

**Demo Highlights:**
- 📊 Intelligent scoring system with transparent justifications
- 🎯 Semantic matching beyond simple keyword search
- 💡 AI-powered skill extraction and analysis
- 🚀 Complete full-stack application workflow

---

### Video Demo Recording Guide

1. **Setup** (30 seconds):
   - Show the application structure
   - Start the backend server
   - Open the frontend

2. **Upload Resumes** (45 seconds):
   - Upload 2-3 sample resumes
   - Show successful upload confirmations
   - Highlight extracted candidate information

3. **Job Matching** (45 seconds):
   - Enter a job title and description
   - Click "Find Best Matches"
   - Show the results with scores and justifications

4. **Results Analysis** (30 seconds):
   - Highlight key matches and gaps
   - Show how scores are calculated
   - Demonstrate filtering by threshold

### Sample Job Descriptions

See `samples/job_descriptions/` for example job postings to use in demos.

## 📁 Project Structure

```
smart-resume-screener/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
│
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── resume_parser.py      # PDF/TXT parsing
│   ├── data_extractor.py     # LLM data extraction
│   └── job_matcher.py        # LLM job matching
│
├── database/                  # Database layer
│   ├── __init__.py
│   └── db_manager.py         # SQLite operations
│
├── frontend/                  # Web interface
│   └── index.html            # Single-page application
│
├── uploads/                   # Resume upload directory
│   └── resumes/              # Uploaded resume files
│
├── data/                      # Application data
│   └── resumes.db            # SQLite database
│
└── samples/                   # Sample data for testing
    ├── resumes/              # Sample resume files
    └── job_descriptions/     # Sample job postings
```

## 🔍 Code Quality & Structure

### Design Patterns:
- **Service Layer Pattern**: Separation of business logic
- **Repository Pattern**: Database abstraction
- **Single Responsibility**: Each module has one clear purpose

### Best Practices:
- **Error Handling**: Comprehensive try-catch blocks
- **Validation**: Input validation at API layer
- **Documentation**: Detailed docstrings for all functions
- **Type Safety**: Clear parameter types and return values
- **Configuration**: Environment-based configuration

## 🧪 Testing

### Manual Testing:

1. Test with various resume formats (PDF, TXT)
2. Test with different job descriptions
3. Test threshold filtering
4. Test with resumes missing information

### Sample Test Cases:

```python
# Test resume parsing
- Valid PDF resume → Success
- Invalid PDF → Error handling
- TXT resume → Success

# Test data extraction
- Complete resume → All fields extracted
- Minimal resume → Fallback values used

# Test job matching
- Perfect match → Score 9-10
- No match → Score 1-2
- Partial match → Score 5-7
```

## 🚀 Deployment

### Production Considerations:

1. **Security**:
   - Use environment variables for API keys
   - Implement rate limiting
   - Add authentication for API endpoints

2. **Scalability**:
   - Use PostgreSQL instead of SQLite
   - Add Redis for caching
   - Deploy with Gunicorn/uWSGI

3. **Monitoring**:
   - Add logging (Python logging module)
   - Monitor API response times
   - Track LLM token usage

### Docker Deployment (Optional):

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- OpenAI for GPT API
- Flask framework
- pdfplumber for PDF parsing

## 📞 Support

For questions or issues:
1. Check the README
2. Review the code comments
3. Check API error messages

## 🎓 Learning Outcomes

This project demonstrates:
- Full-stack development (Python backend + HTML/JS frontend)
- RESTful API design
- LLM integration and prompt engineering
- Database design and management
- File handling and parsing
- Error handling and validation
- Clean code architecture

---

**Built with ❤️ for intelligent resume screening**

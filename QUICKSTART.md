# 🚀 Quick Start Guide

Get the Smart Resume Screener running in 5 minutes!

## Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation Steps

### 1️⃣ Navigate to Project Directory
```bash
cd c:\Users\nehal\Desktop\HPE\smart-resume-screener
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables
```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your OpenAI API key
notepad .env
```

Add this to `.env`:
```
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
DATABASE_PATH=data/resumes.db
```

### 6️⃣ Run Setup Script
```bash
python setup.py
```

### 7️⃣ Start the Application
```bash
python app.py
```

You should see:
```
✅ Database initialized successfully
🚀 Starting Smart Resume Screener API...
📍 API available at: http://localhost:5000
✅ Health check: http://localhost:5000/health
 * Running on http://0.0.0.0:5000
```

### 8️⃣ Open the Frontend

Open `frontend/index.html` in your web browser, or:

```bash
cd frontend
python -m http.server 8000
```

Then visit: http://localhost:8000

## 🎯 Try It Out!

### Option 1: Use Sample Data

1. **Upload Resumes:**
   - Click "Choose Files"
   - Navigate to `samples/resumes/`
   - Select all 3 `.txt` files
   - Click "Upload Resumes"

2. **Enter Job Description:**
   - Copy content from `samples/job_descriptions/senior_fullstack_engineer.txt`
   - Paste into the job description field
   - Add job title: "Senior Full Stack Engineer"

3. **Find Matches:**
   - Click "Find Best Matches"
   - View the results!

### Option 2: Use Your Own Data

1. Upload your own resume (PDF or TXT format)
2. Paste any job description
3. See how well it matches!

## 🎥 Record Your Demo

Follow the `DEMO_SCRIPT.md` to record your 2-3 minute video demonstration.

## 🧪 Testing

Run through the test scenarios in `TESTING.md` to ensure everything works correctly.

## ❓ Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"
Check your `.env` file has the correct key.

### Port 5000 already in use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :5000
kill -9 <PID>
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [TESTING.md](TESTING.md) for comprehensive test cases
- Review [DEMO_SCRIPT.md](DEMO_SCRIPT.md) for video recording guide

## 🎉 You're All Set!

Start screening resumes intelligently with AI! 🚀

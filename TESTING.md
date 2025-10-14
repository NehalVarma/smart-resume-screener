# Testing Guide for Smart Resume Screener

## 🧪 Testing Checklist

### Pre-Testing Setup

1. **Environment Setup**
   ```bash
   # Activate virtual environment
   venv\Scripts\activate  # Windows
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Configure .env file
   cp .env.example .env
   # Add your OPENAI_API_KEY
   ```

2. **Run Setup Script**
   ```bash
   python setup.py
   ```

3. **Start Backend**
   ```bash
   python app.py
   ```
   Expected output:
   ```
   ✅ Database initialized successfully
   🚀 Starting Smart Resume Screener API...
   📍 API available at: http://localhost:5000
   ✅ Health check: http://localhost:5000/health
   ```

---

## 🔍 Manual Testing Scenarios

### Test 1: Health Check
**Objective:** Verify API is running

**Steps:**
1. Open browser
2. Navigate to: `http://localhost:5000/health`

**Expected Result:**
```json
{
  "status": "healthy",
  "service": "Smart Resume Screener API"
}
```

---

### Test 2: Upload Resume (TXT)
**Objective:** Test text resume upload and parsing

**Steps:**
1. Open `frontend/index.html`
2. Click "Choose Files"
3. Select `samples/resumes/john_doe_software_engineer.txt`
4. Click "Upload Resumes"

**Expected Results:**
- ✅ Success message appears
- ✅ Candidate name "John Doe" displayed
- ✅ Extracted data includes:
  - Name
  - Skills (Python, JavaScript, React, etc.)
  - Experience entries
  - Education

**Verification:**
```bash
# Check API endpoint
curl http://localhost:5000/api/candidates
```

---

### Test 3: Upload Multiple Resumes
**Objective:** Test batch upload

**Steps:**
1. Select all 3 sample resumes:
   - john_doe_software_engineer.txt
   - sarah_chen_data_scientist.txt
   - michael_rodriguez_devops.txt
2. Click "Upload Resumes"

**Expected Results:**
- ✅ "Successfully uploaded 3 resume(s)"
- ✅ All 3 names displayed
- ✅ No errors

---

### Test 4: Job Matching - Perfect Match
**Objective:** Test high score matching

**Setup:**
- Upload: `john_doe_software_engineer.txt`
- Job Description: `samples/job_descriptions/senior_fullstack_engineer.txt`

**Steps:**
1. Upload John Doe's resume
2. Enter job title: "Senior Full Stack Engineer"
3. Paste job description
4. Set threshold: 6.0
5. Click "Find Best Matches"

**Expected Results:**
- ✅ Score: 7.5-9.0 (high match)
- ✅ Justification mentions:
  - Python and JavaScript experience
  - React knowledge
  - Years of experience match
- ✅ Key matches include relevant skills
- ✅ Minimal or no gaps

---

### Test 5: Job Matching - Poor Match
**Objective:** Test low score matching

**Setup:**
- Upload: `sarah_chen_data_scientist.txt`
- Job Description: `samples/job_descriptions/devops_sre_engineer.txt`

**Steps:**
1. Upload Sarah Chen's resume (Data Scientist)
2. Enter DevOps Engineer job description
3. Click "Find Best Matches"

**Expected Results:**
- ✅ Score: 2.0-5.0 (low match)
- ✅ Justification mentions skill mismatch
- ✅ Few key matches
- ✅ Many gaps listed

---

### Test 6: Threshold Filtering
**Objective:** Test threshold functionality

**Setup:**
- Upload all 3 resumes
- Job: "Senior Full Stack Engineer"

**Test Cases:**

**Case A: Threshold = 8.0**
- Expected: Only top candidates (1-2 results)

**Case B: Threshold = 5.0**
- Expected: More candidates (2-3 results)

**Case C: Threshold = 10.0**
- Expected: Possibly 0 results (very strict)

---

### Test 7: Error Handling - No OpenAI Key
**Objective:** Test error handling

**Steps:**
1. Remove or invalidate `OPENAI_API_KEY` in `.env`
2. Restart server
3. Try to upload resume

**Expected Result:**
- ✅ Clear error message about API key
- ❌ Application doesn't crash

---

### Test 8: Error Handling - Invalid File
**Objective:** Test file validation

**Steps:**
1. Try to upload a .docx or .jpg file

**Expected Result:**
- ✅ Error: "Invalid file type. Only PDF and TXT allowed"
- ❌ File not processed

---

### Test 9: Empty Job Description
**Objective:** Test validation

**Steps:**
1. Upload resume
2. Leave job description empty
3. Click "Find Best Matches"

**Expected Result:**
- ✅ Error: "Please enter a job description"
- ❌ No API call made

---

### Test 10: Multiple Job Matches
**Objective:** Test job history

**Steps:**
1. Upload 3 resumes
2. Match with first job description
3. Match with second job description
4. Check: `http://localhost:5000/api/job-history`

**Expected Results:**
- ✅ Two job entries
- ✅ Each with correct match count
- ✅ Timestamps present

---

## 🎯 Expected Behavior Summary

### Resume Upload
- **File Types:** PDF, TXT only
- **Max Size:** 16MB
- **Response Time:** < 10 seconds per resume
- **Success Rate:** 99%+ for well-formatted resumes

### Data Extraction
- **Fields Extracted:**
  - Name ✓
  - Contact info ✓
  - Skills (5-20 items) ✓
  - Experience (1-5 entries) ✓
  - Education (1-3 entries) ✓

### Job Matching
- **Response Time:** 5-15 seconds for 1-5 candidates
- **Score Range:** 0.0 - 10.0
- **Justification Length:** 100-300 words
- **Key Matches:** 3-5 items
- **Gaps:** 0-5 items

---

## 🐛 Common Issues & Solutions

### Issue 1: "Import Error" on startup
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 2: "OpenAI API Key not found"
**Solution:**
1. Create `.env` file from `.env.example`
2. Add valid API key
3. Restart server

### Issue 3: "CORS Error" in browser
**Solution:**
- Ensure Flask-CORS is installed
- Check app.py has `CORS(app)`

### Issue 4: Slow matching (>30 seconds)
**Possible Causes:**
- Large resume files
- Many candidates
- Slow OpenAI API response

**Solution:**
- Use gpt-3.5-turbo instead of gpt-4
- Process candidates in smaller batches

### Issue 5: Database errors
**Solution:**
```bash
# Delete and recreate database
rm data/resumes.db
python setup.py
```

---

## 📊 Performance Benchmarks

### Expected Performance:
- **Resume Upload:** 2-5 seconds
- **Data Extraction:** 3-8 seconds
- **Single Match:** 4-10 seconds
- **Batch Match (5 candidates):** 20-50 seconds

### LLM Token Usage (Approximate):
- **Data Extraction:** 500-1000 tokens per resume
- **Job Matching:** 800-1500 tokens per candidate
- **Cost:** ~$0.01-0.03 per resume processing

---

## ✅ Final Verification

Before submitting, verify:

- [ ] All 3 sample resumes upload successfully
- [ ] Data extraction works for each resume
- [ ] Job matching returns reasonable scores
- [ ] Justifications are coherent and relevant
- [ ] UI displays results correctly
- [ ] No console errors
- [ ] README is complete and accurate
- [ ] Code is well-commented
- [ ] Git repository is initialized
- [ ] .env.example provided (not .env)

---

## 🎥 Demo Recording Checklist

- [ ] Backend running without errors
- [ ] Frontend loads without console errors
- [ ] Sample data ready
- [ ] Practiced demo script
- [ ] Recording software configured
- [ ] Audio quality tested
- [ ] Screen resolution: 1920x1080

---

## 📝 Testing Log Template

```
Date: __________
Tester: __________

Test Case | Status | Notes
----------|--------|-------
Health Check | ✅/❌ | 
Upload TXT | ✅/❌ |
Upload PDF | ✅/❌ |
Data Extraction | ✅/❌ |
Job Match (High) | ✅/❌ |
Job Match (Low) | ✅/❌ |
Threshold Filter | ✅/❌ |
Error Handling | ✅/❌ |

Overall Status: ✅ PASS / ❌ FAIL
```

---

## 🚀 Production Readiness Checklist

For production deployment (bonus):

- [ ] Environment variables properly configured
- [ ] Database migrations handled
- [ ] API rate limiting implemented
- [ ] Logging configured
- [ ] Error monitoring (e.g., Sentry)
- [ ] HTTPS configured
- [ ] Authentication added
- [ ] Input sanitization
- [ ] File size limits enforced
- [ ] Backup strategy in place

---

**Happy Testing! 🎉**

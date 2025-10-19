# 🚀 PythonAnywhere Deployment Guide

## Why PythonAnywhere for Your Portfolio?
- ✅ **Always Online** - No cold starts, always accessible
- ✅ **Free Forever** - Perfect for portfolio demos
- ✅ **Easy Setup** - No system dependencies needed
- ✅ **Better File Handling** - Reliable file uploads
- ✅ **Python-Optimized** - Built for Flask apps
- ✅ **Professional URL** - `https://yourusername.pythonanywhere.com`

---

## 📋 Step-by-Step Deployment

### Step 1: Create PythonAnywhere Account
1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Sign up for the **FREE Beginner account**
3. Verify your email

### Step 2: Open Bash Console
1. After login, go to the **Dashboard**
2. Click on **"Consoles"** tab
3. Click **"Bash"** to open a new console

### Step 3: Clone Your Repository
In the Bash console, run:
```bash
git clone https://github.com/NehalVarma/smart-resume-screener.git
cd smart-resume-screener
```

### Step 4: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Create Web App
1. Go to **"Web"** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"** (not "Flask")
4. Select **Python 3.10**

### Step 7: Configure WSGI File
1. In the **Web** tab, click on the **WSGI configuration file** link
2. Delete all the default content
3. Add this code:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOURUSERNAME/smart-resume-screener'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['PYTHONUNBUFFERED'] = '1'

# Import Flask app
from app import app as application
```

**IMPORTANT:** Replace `YOURUSERNAME` with your actual PythonAnywhere username!

### Step 8: Configure Virtual Environment
1. In the **Web** tab, scroll to **"Virtualenv"** section
2. Enter the path: `/home/YOURUSERNAME/.virtualenvs/myenv`
3. Replace `YOURUSENAME` with your actual username

### Step 9: Set Working Directory
1. In the **Web** tab, find **"Code"** section
2. Set **Source code** to: `/home/YOURUSERNAME/smart-resume-screener`
3. Set **Working directory** to: `/home/YOURUSERNAME/smart-resume-screener`

### Step 10: Create Uploads Directory
Back in the Bash console:
```bash
cd ~/smart-resume-screener
mkdir -p uploads/resumes
chmod 755 uploads
chmod 755 uploads/resumes
```

### Step 11: Reload Web App
1. Go back to **Web** tab
2. Click the big green **"Reload"** button at the top

### Step 12: Test Your App! 🎉
Your app is now live at: `https://YOURUSERNAME.pythonanywhere.com`

---

## 🔄 How to Update Your App

When you make changes and push to GitHub:

1. Open Bash console on PythonAnywhere
2. Run:
```bash
cd ~/smart-resume-screener
git pull origin main
```
3. If you updated requirements.txt:
```bash
workon myenv
pip install -r requirements.txt
```
4. Go to **Web** tab and click **Reload**

---

## 🐛 Troubleshooting

### Issue: "ImportError: No module named 'app'"
**Fix:**
- Check WSGI file has correct path
- Verify virtual environment is set correctly
- Make sure you installed requirements.txt

### Issue: "Permission denied" for uploads
**Fix:**
```bash
cd ~/smart-resume-screener
chmod -R 755 uploads
```

### Issue: Web app shows error
**Check Error Logs:**
1. Go to **Web** tab
2. Click on **Error log** link
3. Look for Python errors
4. Fix and reload

### Issue: Static files not loading
**Fix:**
1. In **Web** tab, add **Static files** mapping:
   - URL: `/static/`
   - Directory: `/home/YOURUSERNAME/smart-resume-screener/frontend`

---

## 📱 Add to Portfolio

### Resume/CV:
```
Smart Resume Screener
https://YOURUSERNAME.pythonanywhere.com

AI-powered resume screening system built with Flask and Python.
Deployed on PythonAnywhere with automated candidate matching.
```

### LinkedIn Projects:
```
Project Name: Smart Resume Screener
URL: https://YOURUSERNAME.pythonanywhere.com
Description: Automated resume screening and candidate matching 
system using AI. Built with Flask, Python, featuring intelligent 
skill extraction and job matching algorithms.
```

---

## 💡 PythonAnywhere Tips

### Free Tier Limitations:
- ✅ Always online (no sleeping!)
- ✅ Custom subdomain
- ⚠️ No custom domain (need paid plan)
- ⚠️ Outbound internet disabled (no external API calls - but your mock services work fine!)
- ⚠️ Limited storage (512MB)

### Keep Your App Updated:
Set up a scheduled task (optional):
1. Go to **Tasks** tab
2. Add daily task at 6:00 UTC:
```bash
cd ~/smart-resume-screener && git pull origin main
```

### Monitor Your App:
- **Web** tab shows request count and CPU usage
- **Error log** shows all Python errors
- **Server log** shows access logs

---

## 🎯 Success Checklist

- [ ] PythonAnywhere account created
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Web app created
- [ ] WSGI file configured
- [ ] Virtual environment path set
- [ ] Uploads directory created with permissions
- [ ] App reloaded
- [ ] Can access homepage
- [ ] Can upload sample resume
- [ ] Can match job description
- [ ] URL added to portfolio/resume

---

## 🚀 You're Live on PythonAnywhere!

Congratulations! Your Smart Resume Screener is now:
✅ Accessible 24/7 from anywhere
✅ Reliable file uploads
✅ No cold starts or sleeping
✅ Professional URL for your portfolio
✅ Ready to impress recruiters!

**Your live URL:**
`https://YOURUSERNAME.pythonanywhere.com`

Share it on:
- LinkedIn projects
- Resume/CV
- GitHub README
- Cover letters
- Portfolio website

Good luck with your job search! 🎉

# 🚀 Render.com Setup Instructions

## ✅ Files Ready for Deployment
Your app is now configured with:
- ✅ `requirements.txt` - Updated with gunicorn and all dependencies
- ✅ `render.yaml` - Render configuration file
- ✅ `Procfile` - Alternative deployment config
- ✅ `app.py` - Updated to work with cloud hosting (PORT environment variable)

## 📋 Deployment Steps on Render

### 1. Create Render Account
Go to: https://render.com/register
- Sign up with GitHub (recommended)
- Authorize Render to access your repositories

### 2. Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect to your GitHub repository: `smart-resume-screener`

### 3. Configure Your Service

**Use these EXACT settings:**

| Setting | Value |
|---------|-------|
| **Name** | `smart-resume-screener` (or your choice) |
| **Region** | Oregon (US West) |
| **Branch** | `main` |
| **Root Directory** | (leave empty) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install --upgrade pip && pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120` |
| **Plan** | **Free** |

### 4. Advanced Settings (Optional but Recommended)

Click **"Advanced"** and add:

**Environment Variables:**
- Key: `PYTHON_VERSION` → Value: `3.11.1`

**Auto-Deploy:**
- ✅ Enable "Auto-Deploy" (deploys automatically when you push to GitHub)

### 5. Deploy!
Click **"Create Web Service"**

## ⏱️ Deployment Timeline
- **Initial Build**: 3-5 minutes
- **Watch the logs**: You'll see installation progress
- **Success message**: "Your service is live 🎉"

## 🔍 What to Watch in Logs

Good signs ✅:
```
==> Downloading...
==> Building...
==> Installing dependencies...
Successfully installed Flask gunicorn...
==> Running 'gunicorn app:app'
[INFO] Starting gunicorn...
[INFO] Booting worker...
✅ Database initialized successfully
```

Bad signs ❌ (and fixes):
```
ERROR: Could not find a version that satisfies...
→ Fix: Check requirements.txt formatting

bash: gunicorn: command not found
→ Fix: Already fixed! Make sure you pushed latest changes

ModuleNotFoundError: No module named 'X'
→ Fix: Add missing module to requirements.txt
```

## 🌐 Your Live URL

Once deployed, your URL will be:
```
https://smart-resume-screener.onrender.com
```
(or whatever name you chose)

## 🧪 Test Your Deployment

1. **Health Check**: Visit `https://your-app.onrender.com/health`
   - Should return: `{"status": "healthy", "service": "Smart Resume Screener API"}`

2. **Frontend**: Visit `https://your-app.onrender.com/`
   - Should show the full web interface

3. **Upload Resume**: Use sample resumes from `/samples/resumes/`

4. **Match Job**: Use sample job descriptions from `/samples/job_descriptions/`

## ⚠️ Important Notes for Free Tier

### Cold Starts
- App sleeps after **15 minutes** of inactivity
- First request after sleep takes **30-50 seconds** to wake up
- Subsequent requests are instant

### Ephemeral Storage
- Database resets when service restarts
- Uploaded files are temporary
- **For production**: Use external database (PostgreSQL) or upgrade plan

### Keep It Awake (Optional)
Use a free uptime monitor:
1. Go to: https://uptimerobot.com
2. Add your Render URL
3. Set to ping every 5 minutes
4. Free tier allows 50 monitors

## 🔄 Update Your Deployment

Super easy! Just push to GitHub:

```powershell
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main
```

Render automatically rebuilds and deploys! ✨

## 📱 Add to Portfolio

### Resume/CV:
```
Smart Resume Screener
https://smart-resume-screener.onrender.com

AI-powered candidate matching system built with Flask and Python.
Deployed on Render with automated CI/CD pipeline.
```

### LinkedIn Projects:
```
Project Name: Smart Resume Screener
URL: https://smart-resume-screener.onrender.com
Description: Automated resume screening and candidate matching 
system using AI. Built with Flask, Python, and deployed on 
Render with full CI/CD pipeline.
```

## 🐛 Troubleshooting

### Issue: Build fails with package errors
**Solution**: 
```powershell
# Test locally first
pip install -r requirements.txt

# If it works locally, push again
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

### Issue: App starts but gives 500 errors
**Check Render logs**:
1. Go to Render dashboard
2. Click your service
3. Click "Logs" tab
4. Look for Python errors

**Common fixes**:
- Missing environment variables
- File path issues (use relative paths)
- Database initialization errors

### Issue: URL shows "Not Found"
**Solution**: 
- Make sure `app.py` has the `@app.route('/')` defined
- Check that `frontend/index.html` exists
- Verify `static_folder='frontend'` in Flask initialization

### Issue: Can't upload files
**Free tier limitation**: Ephemeral storage
**Solution for demo**: 
- Use sample files from repository
- Or mention it's a demo limitation

## 🎯 Success Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Web service deployed
- [ ] Build successful (green checkmark)
- [ ] Health endpoint works
- [ ] Frontend loads
- [ ] Can upload sample resume
- [ ] Can match job description
- [ ] URL added to portfolio/resume

## 🚀 You're Live!

Congratulations! Your Smart Resume Screener is now:
✅ Accessible 24/7 from anywhere
✅ Professional URL for your portfolio
✅ Auto-deploys when you push updates
✅ Ready to impress recruiters!

**Share your success:**
- Add to LinkedIn projects
- Include in resume
- Share with potential employers
- Include in cover letters

Good luck with your job search! 🎉

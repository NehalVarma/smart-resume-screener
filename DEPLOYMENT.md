# 🚀 Deployment Guide - Render.com

## Why Render for Your Portfolio?
- ✅ **Always Online** - Works 24/7, even when your laptop is off
- ✅ **Free Forever** - No credit card needed
- ✅ **Professional URL** - Great for portfolio/resume
- ✅ **Auto-updates** - Push to GitHub, auto-deploys
- ⚠️ **Note**: Free tier sleeps after 15 min inactivity (wakes in 30-50 seconds)

## 📋 Step-by-Step Deployment

### Step 1: Push to GitHub (if not already done)

```powershell
# Initialize git (if needed)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for deployment"

# Create repo on GitHub, then:
git remote add origin https://github.com/NehalVarma/smart-resume-screener.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to** https://render.com
2. **Sign up** (use GitHub login for easy connection)
3. **Click** "New +" → "Web Service"
4. **Connect** your GitHub repository: `smart-resume-screener`
5. **Configure**:
   - **Name**: `smart-resume-screener` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Select **Free**
6. **Click** "Create Web Service"

### Step 3: Wait for Deployment
- Takes 2-5 minutes
- Watch the logs for "Build successful"
- Your app will be live at: `https://smart-resume-screener.onrender.com`

### Step 4: Test Your Live App
1. Visit your Render URL
2. Upload sample resumes from `/samples/resumes/`
3. Try job matching with sample descriptions from `/samples/job_descriptions/`

## 🔄 How to Update Your App

Just push to GitHub:
```powershell
git add .
git commit -m "Update feature"
git push
```

Render will automatically redeploy! 🎉

## 📝 Add to Your Portfolio/Resume

**Live Demo**: https://smart-resume-screener.onrender.com
**GitHub**: https://github.com/NehalVarma/smart-resume-screener

### Sample Description:
```
Smart Resume Screener - AI-Powered Candidate Matching System
• Built with Flask, Python, and AI to automate resume screening
• Extracts skills, experience, and matches candidates to job requirements
• Deployed on Render with automated CI/CD pipeline
• Live Demo: [your-render-url]
```

## ⚡ Tips for Portfolio Demo

1. **Keep it awake**: Visit your URL every few days or add to UptimeRobot (free)
2. **Add sample data**: Pre-load some sample resumes for instant demo
3. **Add README**: Include screenshots and demo video in your GitHub README
4. **Monitor**: Check Render dashboard for any errors

## 🔧 Troubleshooting

### Issue: "Application failed to start"
- Check Render logs
- Verify `requirements.txt` has all packages
- Make sure `gunicorn` is in requirements.txt

### Issue: Database resets
- Free tier has ephemeral storage
- Database resets when service restarts
- For persistent storage, upgrade to paid tier or use external DB

### Issue: Slow first load
- Normal for free tier (cold start)
- Takes 30-50 seconds after 15 min of inactivity
- Consider upgrading to paid tier if needed

## 🎯 Next Steps

1. ✅ Deploy to Render
2. ✅ Test all features
3. ✅ Add URL to your resume/portfolio
4. ✅ Share with recruiters!

Good luck with your portfolio! 🚀

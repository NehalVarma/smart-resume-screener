# ✈️ PRE-FLIGHT CHECKLIST
## Run through this 5 minutes before recording

---

## 🔧 TECHNICAL SETUP

### Backend (PowerShell)
```powershell
# 1. Open PowerShell
# 2. Navigate to project
Set-Location 'c:\Users\nehal\Desktop\HPE\smart-resume-screener'

# 3. Start backend
& '.\venv\Scripts\python.exe' app.py

# 4. Wait for this message:
# ✅ Database initialized successfully
# 🚀 Starting Smart Resume Screener API...
# * Running on http://127.0.0.1:5000
```

**Status:** 
- ☐ Terminal shows "Running on http://127.0.0.1:5000"
- ☐ No error messages

---

### Frontend (Browser)
```
# 1. Open Chrome or Edge
# 2. Go to: http://localhost:8000
# 3. Page should load with "Smart Resume Screener" title
```

**Status:**
- ☐ Page loads successfully
- ☐ No console errors (F12 to check)
- ☐ "Choose Files" button visible

---

### Clear Old Data
```
# On the webpage:
# 1. Click red "🗑️ Clear Database" button
# 2. Click "OK" on confirmation
# 3. Should see: "✅ Database cleared successfully!"
```

**Status:**
- ☐ Database cleared
- ☐ No uploaded files showing
- ☐ Ready for fresh demo

---

## 📁 FILE LOCATIONS

### Resumes (need to upload these)
```
C:\Users\nehal\Desktop\HPE\smart-resume-screener\samples\resumes\
├── john_doe_software_engineer.txt
├── sarah_chen_data_scientist.txt
└── michael_rodriguez_devops.txt
```

**Status:**
- ☐ All 3 files exist
- ☐ Can open folder quickly

---

### Job Description (need to copy from here)
```
C:\Users\nehal\Desktop\HPE\smart-resume-screener\samples\job_descriptions\
└── devops_sre_engineer.txt  ← Use this one!
```

**Status:**
- ☐ File exists
- ☐ Can open with Notepad

---

## 🎥 RECORDING SETUP

### Recording Software
**Option 1 - Windows Game Bar (Built-in):**
- ☐ Press Win+G to open
- ☐ Click "Capture" panel
- ☐ Click the record button (circle)
- ☐ Test: Record 5 seconds, play back

**Option 2 - OBS Studio:**
- ☐ OBS is installed
- ☐ Scene set to "Display Capture" or "Window Capture"
- ☐ Audio input set to your microphone
- ☐ Test recording works

**Option 3 - Loom (Online):**
- ☐ Go to loom.com
- ☐ Install extension
- ☐ Test recording

**Status:**
- ☐ Recording tool ready
- ☐ Microphone working
- ☐ Audio levels good (not too quiet/loud)

---

### Browser Setup
```
# 1. Close ALL other tabs
# 2. Close notifications (Discord, Slack, etc.)
# 3. Press F11 for full-screen mode
# 4. Zoom to 100% (Ctrl+0)
```

**Status:**
- ☐ Only demo tab open
- ☐ Full-screen mode (F11)
- ☐ Clean, distraction-free

---

### VS Code (for code section)
```
# 1. Open VS Code
# 2. Open project: c:\Users\nehal\Desktop\HPE\smart-resume-screener
# 3. Minimize (don't close)
```

**Status:**
- ☐ VS Code open with project
- ☐ Explorer panel showing folder structure
- ☐ README.md accessible

---

## 📱 REFERENCE MATERIALS

### What to have ready:
- ☐ RECORDING_SCRIPT.md open on another device OR printed
- ☐ QUICK_REFERENCE.md on phone
- ☐ This checklist marked off
- ☐ Glass of water nearby

---

## 🎤 AUDIO CHECK

### Microphone Test:
1. ☐ Open Sound Recorder or recording software
2. ☐ Record yourself saying: "Testing, one two three"
3. ☐ Play it back
4. ☐ Audio is clear, not muffled
5. ☐ Volume is good (not too quiet)
6. ☐ No background noise (close windows, turn off fans)

---

## 🏃 DRY RUN (PRACTICE)

### Do this ONCE before recording:
```
1. ☐ Say the intro out loud
2. ☐ Upload 3 resumes (actually do it)
3. ☐ Paste job description
4. ☐ Click "Find Best Matches"
5. ☐ Wait for results
6. ☐ Check scores look good (Michael ~9.3, John ~6.1)
7. ☐ Say the outro

Total time: _____ (should be 2-3 minutes)
```

**If dry run worked:**
- ☐ Results show correctly
- ☐ Scores are realistic
- ☐ Timing is under 3 minutes
- ☐ Ready to record for real!

**If dry run had issues:**
- ☐ Restart backend
- ☐ Clear database
- ☐ Try again

---

## 🧘 MENTAL PREP

### Before clicking record:
- ☐ Read intro 3 times
- ☐ Take 3 deep breaths
- ☐ Relax shoulders
- ☐ Smile (improves voice tone!)
- ☐ Remember: You can do multiple takes!

---

## 🚨 EMERGENCY TROUBLESHOOTING

### Backend not starting?
```powershell
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Kill process if needed, then restart
& '.\venv\Scripts\python.exe' app.py
```

### Frontend not loading?
```powershell
# Restart HTTP server
Set-Location 'c:\Users\nehal\Desktop\HPE\smart-resume-screener\frontend'
& '..\venv\Scripts\python.exe' -m http.server 8000
```

### Upload failing?
- Check backend is running
- Check browser console (F12) for errors
- Try refreshing page (Ctrl+R)

### Matching showing duplicates?
- Click "Clear Database" button
- Refresh page
- Upload again

---

## ✅ FINAL GO/NO-GO

### All systems check:
- ☐ Backend running (terminal shows "Running on...")
- ☐ Frontend loaded (browser shows app)
- ☐ Database cleared (no old files)
- ☐ Recording software ready
- ☐ Microphone working
- ☐ Browser full-screen (F11)
- ☐ Notifications off
- ☐ Script ready
- ☐ Practiced once
- ☐ Calm and ready

---

## 🎬 COUNTDOWN TO RECORD

### 5... Clear your throat
### 4... Take a deep breath
### 3... Put on a smile
### 2... Position your cursor at top of page
### 1... Hit record!

---

## 🌟 YOU'RE READY!

### Remember:
- Speak clearly at 80% normal speed
- Pause briefly after key points
- Show the scores and results clearly
- Don't worry about being perfect
- You can always record again!

### If you mess up:
- DON'T say "oops" or apologize
- Just pause recording
- Take a breath
- Start again from that section

---

## 📊 POST-RECORDING CHECKLIST

### After you stop recording:
- ☐ Watch the playback
- ☐ Check audio is clear
- ☐ Check screen is visible
- ☐ Check timing (2-3 minutes)
- ☐ Are you happy with it?

### If YES:
- ☐ Save the video file
- ☐ Give it a good name: "Smart_Resume_Screener_Demo.mp4"
- ☐ Upload to required platform
- ☐ Celebrate! 🎉

### If NO:
- ☐ Note what to improve
- ☐ Clear database again
- ☐ Take a 2-minute break
- ☐ Try again!

---

## 💪 CONFIDENCE BOOSTERS

### Remember:
1. ✅ You built a complete, working application
2. ✅ The demo is straightforward
3. ✅ You understand your code
4. ✅ The app actually works!
5. ✅ You've practiced
6. ✅ Multiple takes are allowed
7. ✅ You got this! 🚀

---

**Now go make an awesome demo! You've got this! 🌟**

Print this checklist or keep it on your phone!

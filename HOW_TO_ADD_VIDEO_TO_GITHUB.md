# 📹 How to Add Video Directly to GitHub README

## ✅ RECOMMENDED METHOD: GitHub Video Upload (Drag & Drop)

GitHub now supports **drag-and-drop video** directly in README files!

### 🎯 Step-by-Step Instructions:

#### **Step 1: Prepare Your Video**
Your video file should be:
- ✅ **Format**: `.mp4`, `.mov`, or `.webm`
- ✅ **Size**: Under **100MB** (GitHub limit)
- ✅ **Duration**: 2-3 minutes is perfect
- ✅ **Location**: Know where your video file is saved

If your video is too large, compress it:
- Use HandBrake (free): https://handbrake.fr/
- Or online: https://www.freeconvert.com/video-compressor

---

#### **Step 2: Edit README on GitHub Website**

1. **Go to your GitHub repository:**
   ```
   https://github.com/NehalVarma/smart-resume-screener
   ```

2. **Click on `README.md`**

3. **Click the ✏️ (Edit) button** in the top right

---

#### **Step 3: Drag & Drop Video**

1. In the editor, **scroll to the Demo Video section** (around line 320)

2. **Find this line:**
   ```markdown
   **[🎥 Click here to watch the demo video](YOUR_VIDEO_LINK_HERE)**
   ```

3. **Replace it with this:**
   ```markdown
   ### 📺 Demo Video

   > Watch the complete demonstration below (2-3 minutes)
   ```

4. **Drag and drop your video file** into the editor
   - GitHub will show "Uploading..." message
   - Wait for upload to complete
   - It will generate a video embed code like:
   ```markdown
   https://github.com/user-attachments/assets/[unique-id]/video.mp4
   ```

5. **The final code should look like:**
   ```markdown
   ### 📺 Demo Video

   > Watch the complete demonstration below (2-3 minutes)

   https://github.com/user-attachments/assets/abc123/smart-resume-demo.mp4
   ```

---

#### **Step 4: Save Changes**

1. **Scroll to bottom**
2. **Add commit message:** "Add demo video to README"
3. **Click "Commit changes"**
4. **Done!** Video will play directly in README

---

## 🎬 ALTERNATIVE METHOD: Use Issues/PR to Upload

If drag-and-drop doesn't work:

### **Step 1: Create a New Issue**
1. Go to: https://github.com/NehalVarma/smart-resume-screener/issues/new
2. Title: "Demo Video Upload"
3. In the comment box, **drag and drop your video**
4. GitHub uploads it and gives you a URL
5. **Copy that URL** (it looks like: `https://github.com/user-attachments/assets/...`)
6. **Don't save the issue** - just close the tab

### **Step 2: Add to README**
1. Edit README.md
2. Replace `YOUR_VIDEO_LINK_HERE` with the copied URL
3. Commit changes

---

## 📝 UPDATE README WITH VIDEO EMBED

Here's the exact code to replace in your README:

### **FIND THIS (around line 320):**
```markdown
## 🎬 Demo Video

### 📺 Watch the Demo

**[🎥 Click here to watch the demo video](YOUR_VIDEO_LINK_HERE)**

The demo showcases:
- ✅ Resume upload and parsing
- ✅ AI-powered data extraction
- ✅ Semantic job matching
- ✅ Scoring and justifications
- ✅ Complete application workflow
```

### **REPLACE WITH THIS:**
```markdown
## 🎬 Demo Video

### 📺 Watch the Complete Demonstration

> 2-3 minute walkthrough of the Smart Resume Screener in action

[Your video will appear here after drag-and-drop upload]

**What you'll see:**
- ✅ **Resume Upload**: Uploading multiple resumes (PDF/TXT)
- ✅ **AI Parsing**: Real-time data extraction with LLM
- ✅ **Job Matching**: Semantic analysis and scoring
- ✅ **Results Display**: Match scores, justifications, and key insights
- ✅ **Code Walkthrough**: Architecture and implementation details

---
```

---

## 🎥 VIDEO EMBED FORMATS

Once uploaded, GitHub supports these formats:

### **Option 1: Direct URL (Recommended)**
```markdown
https://github.com/user-attachments/assets/[id]/video.mp4
```
✅ Auto-plays in README
✅ No external dependencies
✅ Fast loading

### **Option 2: HTML5 Video Tag**
```html
<video src="https://github.com/user-attachments/assets/[id]/video.mp4" controls>
  Your browser does not support the video tag.
</video>
```
✅ More control (controls, autoplay, etc.)
✅ Works in GitHub README

### **Option 3: With Thumbnail**
```markdown
[![Demo Video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](VIDEO_URL)
```
✅ Shows preview image
✅ Clickable to play

---

## 🚀 QUICK ACTION PLAN

### **RIGHT NOW - Do This:**

1. **Locate your video file** on your computer
2. **Check file size** (must be < 100MB)
3. If too large, compress it using HandBrake

### **Then:**

4. **Go to GitHub**: https://github.com/NehalVarma/smart-resume-screener
5. **Click README.md** → **Edit (✏️ icon)**
6. **Scroll to Demo Video section** (line ~320)
7. **Drag and drop your video** into the editor
8. **Wait for upload** (shows progress)
9. **Position the video embed** where you want it
10. **Commit changes** with message: "Add demo video"

---

## 💡 PRO TIPS

### **Video Quality:**
- ✅ Use 1920x1080 resolution
- ✅ Keep file under 50MB for fast loading
- ✅ Use MP4 format (best compatibility)
- ✅ Test playback before uploading

### **README Placement:**
- ✅ Put video **early** in README (after overview)
- ✅ Add descriptive text above/below
- ✅ Include timestamps if video is longer

### **Compression Settings (if needed):**
```
Format: MP4
Video Codec: H.264
Resolution: 1920x1080
Bitrate: 2000-3000 kbps
Frame Rate: 30fps
Audio: AAC, 128kbps
```

---

## 🎯 EXACT STEPS (Copy-Paste Checklist)

```
☐ 1. Open https://github.com/NehalVarma/smart-resume-screener
☐ 2. Click README.md file
☐ 3. Click ✏️ Edit button (top right)
☐ 4. Scroll to line ~320 (Demo Video section)
☐ 5. Delete the line: **[🎥 Click here to watch the demo video](YOUR_VIDEO_LINK_HERE)**
☐ 6. Type: "### 📺 Demo Video" (if not there)
☐ 7. Press Enter twice
☐ 8. Drag your video file from folder into the editor
☐ 9. Wait for "Uploading..." to complete
☐ 10. See the video URL appear (https://github.com/user-attachments/...)
☐ 11. Scroll to bottom
☐ 12. Commit message: "Add demo video to README"
☐ 13. Click "Commit changes"
☐ 14. Refresh README page
☐ 15. Video should play directly in README! 🎉
```

---

## 🆘 TROUBLESHOOTING

### **Video too large (> 100MB)?**
**Solution:**
1. Download HandBrake: https://handbrake.fr/
2. Open your video
3. Select "Fast 1080p30" preset
4. Click "Start"
5. New file will be smaller

### **Upload fails?**
**Solution:**
- Check internet connection
- Try different browser (Chrome works best)
- Try the "Issue upload" method instead

### **Video doesn't play?**
**Solution:**
- Make sure it's MP4 format
- Check if URL is correct
- Clear browser cache and refresh

### **Still not working?**
**Alternative:** Upload to YouTube (Unlisted) and embed:
```markdown
[![Demo Video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
```

---

## 📊 BEFORE & AFTER EXAMPLE

### **BEFORE (What you have now):**
```markdown
**[🎥 Click here to watch the demo video](YOUR_VIDEO_LINK_HERE)**
```
❌ Requires external link
❌ User has to leave GitHub

### **AFTER (What you want):**
```markdown
### 📺 Demo Video

https://github.com/user-attachments/assets/abc123def456/smart-resume-screener-demo.mp4

**What you'll see:**
- Resume upload and AI parsing
- Semantic job matching
- Scoring and results display
```
✅ Video plays directly in README
✅ No external links needed
✅ Professional presentation

---

## 🎬 YOU'RE READY!

**Next steps:**
1. Find your video file
2. Go to GitHub
3. Edit README.md
4. Drag & drop video
5. Commit
6. Celebrate! 🎉

**Your README will look amazing with an embedded demo video!**

---

## 📞 NEED HELP?

If you get stuck:
1. Check video file size (< 100MB)
2. Try Chrome browser
3. Use the "Issue upload" alternative method
4. Or upload to YouTube as backup

**Good luck! You're almost done! 🚀**

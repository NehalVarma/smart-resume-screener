# Git Commands for Smart Resume Screener

## Initial Setup

### Initialize Git Repository
```bash
cd c:\Users\nehal\Desktop\HPE\smart-resume-screener
git init
```

### Add All Files
```bash
git add .
```

### First Commit
```bash
git commit -m "Initial commit: Smart Resume Screener with AI-powered matching"
```

## Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named: `smart-resume-screener`
3. Don't initialize with README (we already have one)

## Connect to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/smart-resume-screener.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Subsequent Commits

```bash
# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "Your commit message here"

# Push to GitHub
git push
```

## Recommended Commit Messages

- "Initial commit: Smart Resume Screener with AI-powered matching"
- "Add resume parser for PDF and TXT files"
- "Implement LLM-based data extraction"
- "Add job matching with semantic analysis"
- "Create SQLite database layer"
- "Build REST API endpoints"
- "Add frontend dashboard"
- "Update documentation and README"
- "Add sample data and demo script"
- "Add testing guide and quick start"

## Branch Strategy (Optional)

```bash
# Create feature branch
git checkout -b feature/add-new-feature

# Work on feature...

# Commit changes
git add .
git commit -m "Add new feature"

# Switch back to main
git checkout main

# Merge feature
git merge feature/add-new-feature

# Push to GitHub
git push
```

## Useful Commands

```bash
# View commit history
git log --oneline

# View changes
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View remote URL
git remote -v

# Pull latest changes
git pull origin main
```

## .gitignore Already Configured

The `.gitignore` file is set up to exclude:
- Python cache files (`__pycache__/`)
- Virtual environment (`venv/`)
- Environment variables (`.env`)
- Database files (`*.db`)
- Uploaded files (`uploads/`)
- IDE files (`.vscode/`, `.idea/`)

This ensures sensitive data and unnecessary files aren't committed.

## Repository Structure for GitHub

```
smart-resume-screener/
├── .gitignore
├── README.md
├── QUICKSTART.md
├── DEMO_SCRIPT.md
├── TESTING.md
├── requirements.txt
├── .env.example
├── app.py
├── config.py
├── setup.py
├── services/
├── database/
├── frontend/
└── samples/
```

## Adding a LICENSE (Recommended)

```bash
# Add MIT License
curl https://raw.githubusercontent.com/licenses/license-templates/master/templates/mit.txt > LICENSE

# Or add manually
# Edit LICENSE file with your name and year

git add LICENSE
git commit -m "Add MIT License"
git push
```

## GitHub Features to Use

### 1. Add Topics
In GitHub repository settings, add topics:
- `python`
- `flask`
- `machine-learning`
- `llm`
- `openai`
- `resume-parser`
- `recruitment`
- `ai`

### 2. Update Repository Description
Set description to:
> AI-powered resume screener that intelligently parses resumes and matches candidates with job descriptions using LLMs

### 3. Enable GitHub Pages (Optional)
Host the frontend on GitHub Pages:
1. Go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main, folder: /frontend
4. Your frontend will be available at: `https://YOUR_USERNAME.github.io/smart-resume-screener/`

## Final Checklist Before Pushing

- [ ] `.env` file is NOT committed (check .gitignore)
- [ ] `venv/` is NOT committed
- [ ] All code is properly formatted
- [ ] README.md is complete
- [ ] Sample data is included
- [ ] No sensitive information in code
- [ ] All files have proper comments

## Push to GitHub

```bash
git push origin main
```

Your repository is now live! 🎉

Share the link: `https://github.com/YOUR_USERNAME/smart-resume-screener`

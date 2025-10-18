# 🔄 Development Workflow Guide

## 📊 Branch Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  main (production)  ←──── merge after testing ────┐        │
│       ↓                                            │        │
│   Production App                                   │        │
│   (live users)                                     │        │
│                                                    │        │
│                                                    │        │
│  staging (testing)  ←──── push changes here ───────┘       │
│       ↓                                                     │
│   Staging App                                               │
│   (testing)                                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### First Time Setup

1. **Create staging branch:**
   ```bash
   Double-click: create_staging.bat
   ```

2. **Deploy staging app:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Create new app from `staging` branch
   - URL: `YOUR_USERNAME-fpcalculator-staging`

3. **Deploy production app:**
   - Create another app from `main` branch
   - URL: `YOUR_USERNAME-fpcalculator`

## 📝 Daily Workflow

### Making Changes

```bash
# 1. Switch to staging
Double-click: switch_to_staging.bat

# 2. Make your changes
# Edit files in your IDE...

# 3. Test locally
streamlit run false_positive_calculator.py

# 4. Commit and push
git add .
git commit -m "Add new feature X"
git push origin staging
```

### Testing on Staging

1. Push triggers automatic deployment to staging
2. Visit: `https://YOUR_USERNAME-fpcalculator-staging.streamlit.app`
3. Test all functionality
4. Get feedback

### Deploying to Production

```bash
# When staging is tested and approved
Double-click: promote_to_production.bat
```

This will:
- ✅ Merge staging → main
- ✅ Push to production
- ✅ Trigger production deployment
- ✅ Return you to staging branch

## 🎯 Common Scenarios

### Scenario 1: Small Bug Fix

```bash
# 1. Switch to staging
switch_to_staging.bat

# 2. Fix the bug
# Edit the file...

# 3. Test locally
streamlit run false_positive_calculator.py

# 4. Commit and push
git add .
git commit -m "Fix: Correct PPV calculation for edge case"
git push origin staging

# 5. Test on staging URL
# Visit staging app and verify fix

# 6. Promote to production
promote_to_production.bat
```

### Scenario 2: New Feature

```bash
# 1. Switch to staging
switch_to_staging.bat

# 2. Develop feature
# Add new functionality...

# 3. Test thoroughly locally
streamlit run false_positive_calculator.py

# 4. Commit with descriptive message
git add .
git commit -m "Feature: Add ROC curve visualization"
git push origin staging

# 5. Test on staging
# Share staging URL with team for feedback

# 6. Iterate if needed
# Make adjustments based on feedback
git add .
git commit -m "Refine ROC curve colors"
git push origin staging

# 7. When approved, promote
promote_to_production.bat
```

### Scenario 3: Multiple Changes

```bash
# Make several commits to staging
git add .
git commit -m "Update: Improve UI layout"
git push origin staging

git add .
git commit -m "Feature: Add export to PDF"
git push origin staging

git add .
git commit -m "Fix: Mobile responsiveness"
git push origin staging

# Test all changes on staging

# Promote all at once
promote_to_production.bat
```

### Scenario 4: Emergency Hotfix

```bash
# 1. Switch to main (production)
switch_to_main.bat

# 2. Make critical fix
# Edit the file...

# 3. Commit and push
git add .
git commit -m "Hotfix: Critical security patch"
git push origin main

# 4. Sync fix back to staging
git checkout staging
git merge main
git push origin staging
```

## 🔍 Checking Status

### Current Branch
```bash
git branch --show-current
```

### Uncommitted Changes
```bash
git status
```

### Commit History
```bash
git log --oneline -10
```

### Compare Branches
```bash
# See what's in staging but not in main
git log main..staging --oneline

# See what's in main but not in staging
git log staging..main --oneline
```

## 🛠️ Helper Scripts Reference

| Script                        | Purpose                                    |
|-------------------------------|-------------------------------------------|
| `create_staging.bat`          | Initial setup - creates staging branch    |
| `switch_to_staging.bat`       | Switch to staging for development         |
| `switch_to_main.bat`          | Switch to main (production)               |
| `promote_to_production.bat`   | Merge staging to main and deploy          |
| `git_setup.bat`               | Initialize Git repository                 |
| `git_push.bat`                | Push to GitHub (first time)               |

## ⚠️ Important Rules

### DO ✅
- Always develop on `staging` first
- Test thoroughly before promoting
- Use descriptive commit messages
- Pull before pushing
- Keep commits atomic (one logical change)

### DON'T ❌
- Never push untested code to `main`
- Don't skip the staging environment
- Don't force push to `main`
- Don't commit secrets or credentials
- Don't merge without testing

## 🐛 Troubleshooting

### "Already on staging" error
```bash
# You're already on staging, just pull latest
git pull origin staging
```

### Merge conflicts
```bash
# During promotion, if conflicts occur:
# 1. Open conflicted files
# 2. Look for <<<<<<< HEAD markers
# 3. Resolve conflicts
# 4. Save files
git add .
git commit -m "Resolved merge conflicts"
git push origin main
```

### Forgot which branch you're on
```bash
git branch --show-current
```

### Want to undo last commit (not pushed)
```bash
git reset --soft HEAD~1
```

### Want to discard all local changes
```bash
git checkout -- .
```

## 📈 Advanced: GitHub Actions

The repository includes automated testing:
- Runs on every push to `staging`
- Checks Python syntax
- Validates dependencies
- Ensures app can start

View results in GitHub under "Actions" tab.

## 🎓 Git Basics Reminder

```bash
# See changes
git status

# Stage files
git add filename.py          # Specific file
git add .                    # All files

# Commit
git commit -m "message"

# Push
git push origin staging      # To staging
git push origin main         # To production

# Pull latest
git pull origin staging

# Create branch
git checkout -b feature-name

# Switch branch
git checkout branch-name

# Merge branch
git merge branch-name
```

## 📞 Getting Help

- Check [STAGING_SETUP.md](STAGING_SETUP.md) for detailed setup
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment options
- Open an issue on GitHub for problems

---

**Happy coding!** 🚀 Remember: staging first, production after testing!


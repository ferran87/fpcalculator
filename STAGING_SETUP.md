# 🔄 Staging Environment Setup Guide

This guide explains how to set up a staging environment to test changes before deploying to production.

## 📋 Overview

**Two Environments:**
- **Production** (main branch) → `https://YOUR_USERNAME-fpcalculator.streamlit.app`
- **Staging** (staging branch) → `https://YOUR_USERNAME-fpcalculator-staging.streamlit.app`

## 🚀 Initial Setup

### Step 1: Create Staging Branch

Run these commands in your `fpcalculator` folder:

```bash
# Create and switch to staging branch
git checkout -b staging

# Push staging branch to GitHub
git push -u origin staging

# Switch back to main
git checkout main
```

Or use the provided script: **Double-click `create_staging.bat`**

### Step 2: Deploy Staging App on Streamlit Cloud

1. Go to [https://share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Configure:
   ```
   Repository: YOUR_USERNAME/fpcalculator
   Branch:     staging  ← Important!
   Main file:  false_positive_calculator.py
   App URL:    YOUR_USERNAME-fpcalculator-staging  ← Custom URL
   ```
4. Click **"Deploy!"**

### Step 3: Deploy Production App (if not done)

1. Click **"New app"** again
2. Configure:
   ```
   Repository: YOUR_USERNAME/fpcalculator
   Branch:     main  ← Important!
   Main file:  false_positive_calculator.py
   App URL:    YOUR_USERNAME-fpcalculator  ← Custom URL
   ```
3. Click **"Deploy!"**

## 🔄 Development Workflow

### Making Changes

```bash
# 1. Switch to staging branch
git checkout staging

# 2. Make your changes to the code
# Edit files as needed...

# 3. Test locally
streamlit run false_positive_calculator.py

# 4. Commit changes
git add .
git commit -m "Description of changes"

# 5. Push to staging
git push origin staging
```

### Testing on Staging

1. Wait for Streamlit Cloud to redeploy (1-2 minutes)
2. Visit: `https://YOUR_USERNAME-fpcalculator-staging.streamlit.app`
3. Test all changes thoroughly
4. Get feedback from team/users

### Promoting to Production

Once staging is tested and approved:

```bash
# 1. Switch to main branch
git checkout main

# 2. Merge staging into main
git merge staging

# 3. Push to production
git push origin main

# 4. Switch back to staging for next changes
git checkout staging
```

Or use the provided script: **Double-click `promote_to_production.bat`**

## 📁 Branch Structure

```
main (production)
  ↑
  │ merge after testing
  │
staging (testing)
  ↑
  │ push changes here first
  │
feature branches (optional)
```

## 🛠️ Advanced: Feature Branches

For larger features, create feature branches:

```bash
# Create feature branch from staging
git checkout staging
git checkout -b feature/new-calculator

# Work on feature
# ... make changes ...

# Push feature branch
git push origin feature/new-calculator

# When ready, merge to staging
git checkout staging
git merge feature/new-calculator
git push origin staging

# Delete feature branch after merge
git branch -d feature/new-calculator
git push origin --delete feature/new-calculator
```

## 🔍 Comparing Environments

| Environment | Branch  | URL                                    | Purpose                |
|-------------|---------|----------------------------------------|------------------------|
| Production  | main    | YOUR_USERNAME-fpcalculator             | Live app for users     |
| Staging     | staging | YOUR_USERNAME-fpcalculator-staging     | Test before production |

## 📊 Workflow Scripts

I've created helper scripts for you:

### `create_staging.bat`
- Creates staging branch
- Pushes to GitHub
- Returns to main branch

### `promote_to_production.bat`
- Merges staging to main
- Pushes to production
- Returns to staging branch

### `switch_to_staging.bat`
- Switches to staging branch
- Pulls latest changes

### `switch_to_main.bat`
- Switches to main branch
- Pulls latest changes

## ⚠️ Best Practices

### DO ✅
- Always develop on `staging` branch
- Test thoroughly on staging before promoting
- Keep staging and main in sync
- Use descriptive commit messages
- Pull before pushing to avoid conflicts

### DON'T ❌
- Don't push untested code to `main`
- Don't skip staging environment
- Don't force push to `main` (use `--force-with-lease` if needed)
- Don't merge without testing

## 🐛 Troubleshooting

### Merge Conflicts

If you get merge conflicts when promoting to production:

```bash
# 1. Start the merge
git checkout main
git merge staging

# 2. If conflicts occur, resolve them in your editor
# Look for <<<<<<< HEAD markers

# 3. After resolving, commit
git add .
git commit -m "Merge staging to main - resolved conflicts"

# 4. Push to production
git push origin main
```

### Staging Out of Sync

If staging is behind main:

```bash
# Update staging with main changes
git checkout staging
git merge main
git push origin staging
```

### Reset Staging to Match Main

If staging has issues and you want to reset:

```bash
git checkout staging
git reset --hard main
git push origin staging --force-with-lease
```

## 🔐 Protected Branches (Optional)

On GitHub, you can protect the `main` branch:

1. Go to repository **Settings**
2. Click **Branches**
3. Add rule for `main`
4. Enable:
   - Require pull request reviews
   - Require status checks
   - Include administrators

This forces all changes to go through staging first.

## 📈 Monitoring Both Environments

### Streamlit Cloud Dashboard

From [share.streamlit.io](https://share.streamlit.io):
- View both apps
- Check logs for each
- Monitor resource usage
- Reboot if needed

### GitHub Actions (Optional)

You can add automated testing:
- Run tests on push to staging
- Automated deployment checks
- Notify on successful deployments

## 🎯 Quick Reference

```bash
# Daily workflow
git checkout staging          # Start on staging
# ... make changes ...
git add .
git commit -m "message"
git push origin staging       # Test on staging

# When ready for production
git checkout main
git merge staging
git push origin main          # Deploy to production
git checkout staging          # Back to staging
```

## 📞 Need Help?

- Check logs in Streamlit Cloud
- Review Git documentation
- Open an issue on GitHub
- Check [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Ready to set up staging?** Run `create_staging.bat` or follow Step 1 above! 🚀


# 📤 Publishing Your False Positive Calculator to GitHub

Follow these steps to publish your project to GitHub and make it publicly available.

## Step 1: Initialize Git Repository

Open your terminal in the `fpcalculator` folder and run:

```bash
cd fpcalculator
git init
```

## Step 2: Add All Files

```bash
git add .
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: False Positive Calculator app"
```

## Step 4: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `fpcalculator`
   - **Description**: "A comprehensive Streamlit app for understanding false positive rates in diagnostic testing"
   - **Visibility**: Choose **Public**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 5: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/fpcalculator.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 6: Verify Upload

1. Go to `https://github.com/YOUR_USERNAME/fpcalculator`
2. You should see all your files uploaded
3. GitHub will automatically display your README.md on the main page

## Step 7: Deploy to Streamlit Cloud (Optional but Recommended)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select:
   - **Repository**: `YOUR_USERNAME/fpcalculator`
   - **Branch**: `main`
   - **Main file path**: `false_positive_calculator.py`
5. Click **"Deploy"**
6. Your app will be live at: `https://YOUR_USERNAME-fpcalculator.streamlit.app`

## Step 8: Update README with Live Demo Link

Once deployed, update your README.md:

```bash
# Edit README.md and replace the demo link
git add README.md
git commit -m "Add live demo link"
git push
```

## Step 9: Add Topics to Your Repository (Optional)

On your GitHub repository page:
1. Click the gear icon ⚙️ next to "About"
2. Add topics like:
   - `streamlit`
   - `python`
   - `data-visualization`
   - `statistics`
   - `medical-testing`
   - `false-positives`
   - `bayesian-statistics`
   - `healthcare`
3. Save changes

## Step 10: Share Your Project! 🎉

Your project is now public! Share it:
- On social media (Twitter, LinkedIn)
- In relevant communities (Reddit r/datascience, r/statistics)
- With colleagues and friends
- On your portfolio website

## Future Updates

When you make changes to your app:

```bash
git add .
git commit -m "Description of your changes"
git push
```

If deployed on Streamlit Cloud, it will automatically redeploy with your changes!

## Troubleshooting

### Authentication Issues

If you have trouble pushing, you may need to set up authentication:

**Option 1: Personal Access Token (Recommended)**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Use the token as your password when pushing

**Option 2: SSH Key**
1. Generate SSH key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. Add to GitHub: Settings → SSH and GPG keys
3. Change remote URL: `git remote set-url origin git@github.com:YOUR_USERNAME/fpcalculator.git`

### Large Files

If you have large files (>100MB), use Git LFS:
```bash
git lfs install
git lfs track "*.csv"
git add .gitattributes
```

## Need Help?

- [GitHub Docs](https://docs.github.com)
- [Streamlit Deployment Docs](https://docs.streamlit.io/streamlit-cloud)
- Open an issue in this repository

---

**Congratulations on publishing your project! 🚀**


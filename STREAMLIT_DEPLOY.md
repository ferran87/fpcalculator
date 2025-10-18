# 🚀 Deploy to Streamlit Cloud - Step by Step Guide

## Prerequisites
✅ Your code is pushed to GitHub at `https://github.com/YOUR_USERNAME/fpcalculator`

## Deployment Steps

### Step 1: Go to Streamlit Cloud
1. Open your browser and go to: **[https://share.streamlit.io](https://share.streamlit.io)**
2. Click **"Sign in"** or **"Get started"**
3. Sign in with your **GitHub account**

### Step 2: Create New App
1. Once logged in, click the **"New app"** button (top right)
2. You'll see a form with three main fields

### Step 3: Configure Your App
Fill in the deployment form:

**Repository:**
- Select your repository: `YOUR_USERNAME/fpcalculator`
- If you don't see it, click "Authorize Streamlit" to give access

**Branch:**
- Select: `main` (or `master` if that's your default branch)

**Main file path:**
- Enter: `false_positive_calculator.py`

**App URL (optional):**
- You can customize the URL or leave it as default
- Default will be: `YOUR_USERNAME-fpcalculator.streamlit.app`

### Step 4: Advanced Settings (Optional)
Click "Advanced settings" if you need to:
- Set Python version (default 3.11 is fine)
- Add secrets (not needed for this app)
- Configure custom domains

### Step 5: Deploy!
1. Click the **"Deploy!"** button
2. Wait for the deployment process (usually 2-5 minutes)
3. You'll see logs showing the installation progress

### Step 6: Your App is Live! 🎉
Once deployment is complete:
- Your app will be live at: `https://YOUR_USERNAME-fpcalculator.streamlit.app`
- The page will automatically refresh to show your app
- Share this URL with anyone!

## Automatic Updates

Every time you push changes to your GitHub repository:
1. Streamlit Cloud will automatically detect the changes
2. It will redeploy your app with the latest code
3. No manual redeployment needed!

## Managing Your App

From the Streamlit Cloud dashboard, you can:
- **View logs**: Click on your app → "Manage app" → "Logs"
- **Reboot app**: If something goes wrong, click "Reboot app"
- **Delete app**: Remove the deployment
- **Analytics**: View usage statistics

## Troubleshooting

### App won't deploy
- Check that all files are pushed to GitHub
- Verify `requirements.txt` is present
- Check logs for error messages

### Import errors
- Make sure all dependencies are in `requirements.txt`
- Check Python version compatibility

### App is slow
- Streamlit Cloud free tier has resource limits
- Consider optimizing your code or upgrading

### Can't find repository
- Make sure the repository is public
- Authorize Streamlit to access your GitHub account
- Refresh the page

## Custom Domain (Optional)

To use a custom domain like `fpcalculator.com`:
1. Purchase a domain from a registrar
2. In Streamlit Cloud, go to app settings
3. Add your custom domain
4. Configure DNS records as instructed
5. SSL certificate is automatically provided

## Sharing Your App

Once deployed, share your app:
- Direct link: `https://YOUR_USERNAME-fpcalculator.streamlit.app`
- Add to your GitHub README
- Share on social media
- Add to your portfolio

## Monitoring

Streamlit Cloud provides:
- **Usage analytics**: Number of visitors
- **Error tracking**: View errors in logs
- **Performance metrics**: Load times

## Free Tier Limits

Streamlit Cloud free tier includes:
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ 1 CPU per app
- ✅ Automatic HTTPS
- ✅ Custom domains
- ⚠️ Apps sleep after inactivity (wake on visit)

## Need Help?

- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/YOUR_USERNAME/fpcalculator/issues)

---

**Ready to deploy? Go to [share.streamlit.io](https://share.streamlit.io) now!** 🚀


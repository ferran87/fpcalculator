# Deployment Guide

This guide covers various ways to deploy the False Positive Calculator app.

## Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy your Streamlit app for free.

### Steps:

1. **Push your code to GitHub** (see main README for Git commands)

2. **Sign up for Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository: `yourusername/fpcalculator`
   - Set the main file path: `false_positive_calculator.py`
   - Click "Deploy"

4. **Your app will be live at**: `https://yourusername-fpcalculator.streamlit.app`

### Configuration

The `.streamlit/config.toml` file is already configured for deployment.

## Docker Deployment

### Create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "false_positive_calculator.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and run:

```bash
docker build -t fpcalculator .
docker run -p 8501:8501 fpcalculator
```

## Heroku Deployment

### Prerequisites:
- Heroku account
- Heroku CLI installed

### Files needed:

**setup.sh**:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

**Procfile**:
```
web: sh setup.sh && streamlit run false_positive_calculator.py
```

### Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

## AWS EC2 Deployment

1. **Launch an EC2 instance** (Ubuntu recommended)

2. **SSH into your instance**:
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Install dependencies**:
```bash
sudo apt update
sudo apt install python3-pip
```

4. **Clone and setup**:
```bash
git clone https://github.com/yourusername/fpcalculator.git
cd fpcalculator
pip3 install -r requirements.txt
```

5. **Run with nohup**:
```bash
nohup streamlit run false_positive_calculator.py --server.port 8501 &
```

6. **Configure security group** to allow inbound traffic on port 8501

## Google Cloud Run

1. **Create a Dockerfile** (see Docker section above)

2. **Build and push to Google Container Registry**:
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/fpcalculator
```

3. **Deploy to Cloud Run**:
```bash
gcloud run deploy --image gcr.io/PROJECT-ID/fpcalculator --platform managed
```

## Azure App Service

1. **Create App Service** in Azure Portal

2. **Configure deployment**:
   - Choose GitHub as deployment source
   - Select your repository
   - Configure build settings

3. **Set startup command**:
```
python -m streamlit run false_positive_calculator.py --server.port 8000 --server.address 0.0.0.0
```

## Custom Domain

After deploying to any platform, you can configure a custom domain:

1. **Purchase a domain** (e.g., from Namecheap, GoDaddy)
2. **Configure DNS** to point to your deployment
3. **Set up SSL/TLS** (most platforms offer free SSL)

## Environment Variables

If you need to add environment variables (e.g., for analytics):

**Streamlit Cloud**: Add in the app settings
**Heroku**: `heroku config:set VAR_NAME=value`
**Docker**: Use `-e` flag or `.env` file
**AWS/GCP/Azure**: Configure in the platform's settings

## Monitoring

Consider adding:
- **Google Analytics** for usage tracking
- **Sentry** for error monitoring
- **Uptime monitoring** (e.g., UptimeRobot)

## Troubleshooting

### App won't start
- Check Python version compatibility
- Verify all dependencies are installed
- Check logs for error messages

### Port issues
- Ensure the port is not blocked by firewall
- Use the correct port for your platform

### Memory issues
- Streamlit Cloud: Free tier has 1GB RAM limit
- Consider upgrading or optimizing code

## Need Help?

Open an issue on GitHub if you encounter deployment problems!


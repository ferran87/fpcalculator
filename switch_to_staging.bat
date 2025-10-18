@echo off
echo ========================================
echo Switching to Staging Branch
echo ========================================
echo.

echo Fetching latest changes...
git fetch origin

echo.
echo Switching to staging branch...
git checkout staging

echo.
echo Pulling latest changes...
git pull origin staging

echo.
echo ========================================
echo Now on STAGING branch ✓
echo ========================================
echo.
echo You can now:
echo 1. Make changes to your code
echo 2. Test locally: streamlit run false_positive_calculator.py
echo 3. Commit: git add . && git commit -m "your message"
echo 4. Push: git push origin staging
echo 5. Test on staging URL before promoting to production
echo.
echo Current branch:
git branch --show-current
echo ========================================
pause


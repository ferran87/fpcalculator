@echo off
echo ========================================
echo Pushing All Changes and Creating Staging
echo ========================================
echo.

echo Step 1: Adding all files...
git add .

echo.
echo Step 2: Committing changes...
git commit -m "Refactor: Convert to AB Testing False Positive Calculator for PMs"

echo.
echo Step 3: Pushing to main branch...
git push origin main

echo.
echo Step 4: Creating staging branch...
git checkout -b staging

echo.
echo Step 5: Pushing staging branch...
git push -u origin staging

echo.
echo Step 6: Switching back to main...
git checkout main

echo.
echo ========================================
echo Success! ✓
echo ========================================
echo.
echo Branches created:
echo - main (production)
echo - staging (development)
echo.
echo Both branches are now on GitHub!
echo.
echo Next steps:
echo 1. Deploy staging app: https://share.streamlit.io
echo    - Branch: staging
echo    - URL: YOUR_USERNAME-fpcalculator-staging
echo.
echo 2. Deploy production app: https://share.streamlit.io
echo    - Branch: main
echo    - URL: YOUR_USERNAME-fpcalculator
echo.
echo Use switch_to_staging.bat to start developing!
echo ========================================
pause


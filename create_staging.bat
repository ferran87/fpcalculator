@echo off
echo ========================================
echo Creating Staging Environment
echo ========================================
echo.

echo Step 1: Creating staging branch...
git checkout -b staging

if %ERRORLEVEL% NEQ 0 (
    echo Staging branch might already exist, switching to it...
    git checkout staging
)

echo.
echo Step 2: Pushing staging branch to GitHub...
git push -u origin staging

echo.
echo Step 3: Switching back to main branch...
git checkout main

echo.
echo ========================================
echo Staging Environment Created! ✓
echo ========================================
echo.
echo Next Steps:
echo 1. Go to https://share.streamlit.io
echo 2. Click "New app"
echo 3. Select:
echo    - Repository: YOUR_USERNAME/fpcalculator
echo    - Branch: staging
echo    - Main file: false_positive_calculator.py
echo    - App URL: YOUR_USERNAME-fpcalculator-staging
echo 4. Click "Deploy!"
echo.
echo You now have two environments:
echo - Production: main branch
echo - Staging: staging branch
echo.
echo Use switch_to_staging.bat to work on staging
echo Use promote_to_production.bat to deploy to main
echo ========================================
pause


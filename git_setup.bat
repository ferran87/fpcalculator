@echo off
echo Initializing Git repository...
git init

echo Adding all files...
git add .

echo Creating initial commit...
git commit -m "Initial commit: False Positive Calculator app"

echo.
echo ========================================
echo Git repository initialized successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Create a new repository on GitHub named 'fpcalculator'
echo 2. Then run these commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/fpcalculator.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Replace YOUR_USERNAME with your actual GitHub username
echo ========================================
pause


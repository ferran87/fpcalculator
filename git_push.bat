@echo off
set /p username="Enter your GitHub username: "

echo.
echo Connecting to GitHub repository...
git remote add origin https://github.com/%username%/fpcalculator.git

echo Setting main branch...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Successfully pushed to GitHub!
echo ========================================
echo.
echo Your repository is now live at:
echo https://github.com/%username%/fpcalculator
echo.
pause


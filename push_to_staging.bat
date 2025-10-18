@echo off
echo ========================================
echo Push Changes to Staging Branch
echo ========================================
echo.

echo Current branch:
git branch --show-current
echo.

echo Checking for changes...
git status --short
echo.

set /p confirm="Do you want to push these changes to staging? (yes/no): "

if /i not "%confirm%"=="yes" (
    echo.
    echo Push cancelled.
    pause
    exit /b
)

echo.
echo Step 1: Switching to staging branch...
git checkout staging

echo.
echo Step 2: Adding all changes...
git add .

echo.
echo Step 3: Committing changes...
set /p message="Enter commit message: "
git commit -m "%message%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Step 4: Pushing to staging...
    git push origin staging
    
    echo.
    echo ========================================
    echo Successfully pushed to staging! ✓
    echo ========================================
    echo.
    echo Your changes are now on staging branch.
    echo Streamlit Cloud will automatically redeploy.
    echo.
    echo Staging URL: YOUR_USERNAME-fpcalculator-staging.streamlit.app
    echo.
    echo Test your changes, then use promote_to_production.bat
    echo to deploy to production when ready.
    echo ========================================
) else (
    echo.
    echo No changes to commit or commit failed.
    echo.
)

pause


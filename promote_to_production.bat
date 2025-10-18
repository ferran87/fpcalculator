@echo off
echo ========================================
echo Promote Staging to Production
echo ========================================
echo.

echo This will merge staging branch into main (production)
echo.
set /p confirm="Are you sure? (yes/no): "

if /i not "%confirm%"=="yes" (
    echo.
    echo Promotion cancelled.
    pause
    exit /b
)

echo.
echo Step 1: Switching to main branch...
git checkout main

echo.
echo Step 2: Pulling latest main...
git pull origin main

echo.
echo Step 3: Merging staging into main...
git merge staging -m "Merge staging to production"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ⚠️  MERGE CONFLICT DETECTED!
    echo.
    echo Please resolve conflicts manually:
    echo 1. Open conflicted files in your editor
    echo 2. Look for ^^^^^^^ HEAD markers
    echo 3. Resolve conflicts
    echo 4. Run: git add .
    echo 5. Run: git commit -m "Resolved merge conflicts"
    echo 6. Run: git push origin main
    echo.
    pause
    exit /b
)

echo.
echo Step 4: Pushing to production...
git push origin main

echo.
echo Step 5: Switching back to staging...
git checkout staging

echo.
echo ========================================
echo Successfully Promoted to Production! ✓
echo ========================================
echo.
echo Your changes are now live on:
echo https://YOUR_USERNAME-fpcalculator.streamlit.app
echo.
echo Streamlit Cloud will automatically redeploy (1-2 minutes)
echo.
echo You are now back on staging branch for next changes.
echo ========================================
pause


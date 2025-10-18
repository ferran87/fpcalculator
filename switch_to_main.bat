@echo off
echo ========================================
echo Switching to Main Branch (Production)
echo ========================================
echo.

echo Fetching latest changes...
git fetch origin

echo.
echo Switching to main branch...
git checkout main

echo.
echo Pulling latest changes...
git pull origin main

echo.
echo ========================================
echo Now on MAIN branch (PRODUCTION) ✓
echo ========================================
echo.
echo ⚠️  WARNING: You are on the production branch!
echo.
echo Only push to main after:
echo 1. Testing thoroughly on staging
echo 2. Getting approval
echo 3. Merging from staging
echo.
echo To merge staging to main, use: promote_to_production.bat
echo.
echo Current branch:
git branch --show-current
echo ========================================
pause


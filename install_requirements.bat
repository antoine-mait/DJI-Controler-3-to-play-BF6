@echo off
echo =============================================
echo   Installing DJI Controller dependencies
echo =============================================

pip install --upgrade pip
pip install hidapi vgamepad pywin32

echo.
echo ✅ Installation complete!
echo Run your script with:
echo   python dji_to_xbox.py
echo =============================================
pause

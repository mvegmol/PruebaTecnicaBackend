@echo off
echo Activando el entorno virtual
call venv\Scripts\activate.bat
if %ERRORLEVEL% equ 0 (
    echo Virtual environment activated.
) else (
    echo Failed to activate virtual environment. Make sure it exists.
)

cmd /k "cd /d .. && cd src"

exit
@echo off
echo Creando el entorno virtual

:: Crear el entorno virtual si no existe
if not exist venv (
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo Error: Fallo al crear el entorno virtual
        exit /b 1
    )
    echo Entorno virtual creado con éxito.
) else (
    echo El entorno virtual ya existe.
)

:: Activar el entorno virtual
call venv\Scripts\activate.bat

:: Instalar las dependencias desde requirements.txt
echo Instalando las dependencias...
pip install --upgrade pip
pip install fastapi[standard]
pip install sqlmodel
pip install pydantic
if %ERRORLEVEL% equ 0 (
    echo Instalación completada
) else (
    echo Error: No se completó la instalación de las dependencias
    exit /b 1
)

exit

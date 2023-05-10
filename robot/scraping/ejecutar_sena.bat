@echo off
echo Ejecutando el archivo Python...
Python scraping_sena.py
if %errorlevel%==0 (
    echo El código se ejecutó correctamente.
    echo Enviando alerta...
    REM Comando para enviar una alerta
) else (
    echo Se produjo un error al ejecutar el código.
    pause
)

@ECHO OFF
CALL venv\Scripts\activate.bat
python CRCWorkspace\manage.py runserver
pause
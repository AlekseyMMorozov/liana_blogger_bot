@echo off

call %~d0venv\Scripts\activate

cd %~dp0

python create_bot.py

pause
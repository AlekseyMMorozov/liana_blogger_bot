@echo off

call %~dp0venv\Scripts\activate

cd %~dp0

python liana_bot.python

pause
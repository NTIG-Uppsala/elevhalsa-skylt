@echo off
py -m ensurepip --upgrade
py -m venv env
call env/Scripts/activate
pip install -r requirements.txt
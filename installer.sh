#!/bin/bash

".\python-3.8.10-amd64.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

pip install -r requirements.txt

python -m pip install django

python -m webbrowser http://localhost:7888/

python manage.py runserver 7888
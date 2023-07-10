START "" python-3.8.10-amd64.exe

pip install -r requirements.txt

python -m pip install django

python -m webbrowser http://localhost:7888/

python manage.py runserver 7888
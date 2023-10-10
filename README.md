# Ahora API

> Who is Ahora? 
> he's my Tyler Durden

**Cloud Computing Fall 2023 HW1**


first of all please open `.env.example` and fill the parameters and save it as `.env` file


then install dependencies 
```bash
pip3 install -r requierments.txt
```


don't forget migrate!!!
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```


do it for every installed apps for example
```bash
python3 manage.py makemigrations RequestsService
python3 manage.py migrate RequestsService
```


project works with message broker please run celery
```bash
celery -A ahora_API worker -l info
```



then you have 2 ways to run server:
```bash
python3 manage.py runserver
```
or
```bash
gunicorn --env DJANGO_SETTINGS_MODULE=ahora_API.settings ahora_API.wsgi:application
```



thanks for read this useless readme (you know all of it already)

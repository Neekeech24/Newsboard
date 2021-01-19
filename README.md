# Newsboard
Simple MVP for skill test.


## Installation
Use `git clone Neekeech24/Newsboard` to clone repository

## Usage
You can start API using docker.
Type `docker-compose build` in command line while in project directory
It will show next lines
```
Building web
Step 1/6 : FROM python
 ---> da24d18bf4bf
Step 2/6 : ENV PYTHONUNBOFFERED 1
 ---> Using cache
 ---> e445c039bdbe
Step 3/6 : RUN mkdir /code
 ---> Using cache
 ---> 39b7c919fdb8
Step 4/6 : WORKDIR /code
 ---> Using cache
 ---> 34432b20375c
Step 5/6 : COPY . /code/
 ---> 9f150d64ecd4
Step 6/6 : RUN pip install -r requirements.txt
 ---> Running in 29d6e0da2082
Collecting appdirs==1.4.4
  Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Collecting asgiref==3.3.1
  Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting black==20.8b1
  Downloading black-20.8b1.tar.gz (1.1 MB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Collecting click==7.1.2
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting dj-database-url==0.5.0
  Downloading dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
Collecting Django==3.1.5
  Downloading Django-3.1.5-py3-none-any.whl (7.8 MB)
Collecting django-filter==2.4.0
  Downloading django_filter-2.4.0-py3-none-any.whl (73 kB)
Collecting django-heroku==0.3.1
  Downloading django_heroku-0.3.1-py2.py3-none-any.whl (6.2 kB)
Collecting djangorestframework==3.12.2
  Downloading djangorestframework-3.12.2-py3-none-any.whl (957 kB)
Collecting flake8==3.8.4
  Downloading flake8-3.8.4-py2.py3-none-any.whl (72 kB)
Collecting gunicorn==20.0.4
  Downloading gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
Requirement already satisfied: setuptools>=3.0 in /usr/local/lib/python3.9/site-packages (from gunicorn==20.0.4-
>-r requirements.txt (line 11)) (51.1.2)
Collecting Markdown==3.3.3
  Downloading Markdown-3.3.3-py3-none-any.whl (96 kB)
Collecting mccabe==0.6.1
  Downloading mccabe-0.6.1-py2.py3-none-any.whl (8.6 kB)
Collecting mypy-extensions==0.4.3
  Downloading mypy_extensions-0.4.3-py2.py3-none-any.whl (4.5 kB)
Collecting pathspec==0.8.1
  Downloading pathspec-0.8.1-py2.py3-none-any.whl (28 kB)
Collecting psycopg2==2.8.6
  Downloading psycopg2-2.8.6.tar.gz (383 kB)
Collecting pycodestyle==2.6.0
  Downloading pycodestyle-2.6.0-py2.py3-none-any.whl (41 kB)
Collecting pyflakes==2.2.0
  Downloading pyflakes-2.2.0-py2.py3-none-any.whl (66 kB)
Collecting pytz==2020.5
  Downloading pytz-2020.5-py2.py3-none-any.whl (510 kB)
Collecting regex==2020.11.13
  Downloading regex-2020.11.13-cp39-cp39-manylinux2014_x86_64.whl (732 kB)
Collecting sqlparse==0.4.1
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting toml==0.10.2
  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting typed-ast==1.4.2
  Downloading typed_ast-1.4.2-cp39-cp39-manylinux1_x86_64.whl (769 kB)
Collecting typing-extensions==3.7.4.3
  Downloading typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Collecting whitenoise==5.2.0
  Downloading whitenoise-5.2.0-py2.py3-none-any.whl (19 kB)
Building wheels for collected packages: black, psycopg2
  Building wheel for black (PEP 517): started
  Building wheel for black (PEP 517): finished with status 'done'
  Created wheel for black: filename=black-20.8b1-py3-none-any.whl size=124184 sha256=a45c4ee2848a77d6dcaad2fde1d
aa87a3e6ff5bb327870f3650cc014aefb0721
  Stored in directory: /root/.cache/pip/wheels/4e/57/9a/e704bdd859ee892dc46fff03fd499422dc9e99fd9bd5c446d3
  Building wheel for psycopg2 (setup.py): started
  Building wheel for psycopg2 (setup.py): finished with status 'done'
  Created wheel for psycopg2: filename=psycopg2-2.8.6-cp39-cp39-linux_x86_64.whl size=500230 sha256=7beb1c1cf3c6
ea75f3842f5727fe93cfa95bd6de7125699c8e1d3f8086a574cc
  Stored in directory: /root/.cache/pip/wheels/a2/07/10/a9a82e72d50feb8d646acde6a88000bbf2ca0f82e41aea438a
Successfully built black psycopg2
Installing collected packages: sqlparse, pytz, asgiref, whitenoise, typing-extensions, typed-ast, toml, regex, p
yflakes, pycodestyle, psycopg2, pathspec, mypy-extensions, mccabe, Django, dj-database-url, click, appdirs, Mark
down, gunicorn, flake8, djangorestframework, django-heroku, django-filter, black
Successfully installed Django-3.1.5 Markdown-3.3.3 appdirs-1.4.4 asgiref-3.3.1 black-20.8b1 click-7.1.2 dj-datab
ase-url-0.5.0 django-filter-2.4.0 django-heroku-0.3.1 djangorestframework-3.12.2 flake8-3.8.4 gunicorn-20.0.4 mc
cabe-0.6.1 mypy-extensions-0.4.3 pathspec-0.8.1 psycopg2-2.8.6 pycodestyle-2.6.0 pyflakes-2.2.0 pytz-2020.5 rege
x-2020.11.13 sqlparse-0.4.1 toml-0.10.2 typed-ast-1.4.2 typing-extensions-3.7.4.3 whitenoise-5.2.0
Removing intermediate container 29d6e0da2082
 ---> 6123c3feb5fb

Successfully built 6123c3feb5fb
Successfully tagged newsboard_web:latest
```

Now it is ready to start your API. Type `docker-compose up`.
Visit `127.0.0.1:8000/app` to check your API.


## API endpoints

### Posts
At `127.0.0.1:8000/app/api/posts` you can see all of posts (if they are exist). You can create new one with POST request.

### Comments
At `127.0.0.1:8000/app/api/comments` you can see all of comments to posts (if they are exist). You can create new one with POST request.

### Upvotes
You can upvote any post, using `127.0.0.1:8000/app/api/posts/{post_id}/upvote` endpoint.
Or just click `UP` button on main page (`127.0.0.1:8000/app`)


## Postman collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4f43a8aecdc962294249)

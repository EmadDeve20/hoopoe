# hoopoe

hoopoe is a messengaer app. this is open source and it`s created ``` JUST FOR FUN ```.

I used [this](https://github.com/amirbahador-hub/django_style_guide) repository to make my project structure. 

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd hoopoe
```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- create your env
```
cp .env.example .env
```

5- Create tables
```
python manage.py migrate
```

6- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

7- run the project
```
python manage.py runserver
```

## TODO

- [ ] users models and apis
- [ ] login
- [ ] create SavedMessages
- [ ] use mongodb to save messages
- [ ] send text message to another person (chat but just with text)
- [ ] remove useless packages and update libraries
- [x] use one of GPL LICENSE
- [ ] use pre-commit
- [ ] create github action for (ci/cd)

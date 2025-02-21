# hoopoe

hoopoe is a messengaer app. this is open source and it`s created ``` JUST FOR FUN ```.

I used [this](https://github.com/amirbahador-hub/django_style_guide) repository to make my project structure. 

# Table of contents
1. [project setup](#projec_setup)
2. [TODO list](#todo)


## project setup <a name="projec_setup"></a>

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

## TODO <a name="todo"></a>

- [ ] users models and apis
    - [x] create registering api
    - [x] create profile api to show my profile
    - [x] create another profile api to view profile of another user
    - [x] create api to delete my account
    - [ ] create api to change my password
    - [ ] create an api to set my profile info (bio, email and profile image)
- [ ] login / logout
    - [x] login
    - [ ] logout
- [ ] create SavedMessages
- [ ] use mongodb to save messages
- [ ] send text message to another person (chat but just with text)
- [ ] remove useless packages and update libraries
- [x] use one of GPL LICENSE
- [ ] use pre-commit
- [ ] create github action for (ci/cd)
- [ ] do setting of branches in github
- [ ] create contributing rules in README 
- [ ] add captcha in login

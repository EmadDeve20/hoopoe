# hoopoe

hoopoe is a messengaer app. this is open source and it`s created ``` JUST FOR FUN ```.

I used [this](https://github.com/amirbahador-hub/django_style_guide) repository to make my project structure.

# Table of contents
1. [project setup](#projec_setup)
2. [TODO list](#todo)
3. [Contribute Rules](#contribe)


## project setup <a name="projec_setup"></a>

1 - compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd hoopoe
```

2 - SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3 - install Dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4 - create your env
```
cp .env.example .env
```

5 - Create tables
```
python manage.py migrate
```

6 - Run Initializer Command
```
python manage.py init
```

7 - spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

8 - run the project
```
python manage.py runserver
```

## TODO <a name="todo"></a>

- [x] users models and apis
    - [x] create registering api
    - [x] create profile api to show my profile
    - [x] create another profile api to view profile of another user
    - [x] create api to delete my account
    - [x] create api to change my password
    - [x] create an api to set my profile info (bio, email and profile image)
- [x] login
- [x] create SavedMessages
- [ ] use mongodb to save messages
- [x] send text message to another person (chat but just with text)
- [ ] remove useless packages and update libraries
- [x] use one of GPL LICENSE
- [x] use pre-commit
- [x] create github action for (ci/cd)
- [x] do setting of branches in github
- [x] create contributing rules in README
- [ ] add captcha in login


## Contribute Rules <a name="contribe"></a>

I hope these "Rules" are not be hard.

### branch name

it`s better to set the name of your branch like this:

```emaddeve/feature/UpdateReadme```

Use the tree part for your branch name.
Part one is your name.
The second part is a type of your PR, meaning it`s a fixed bug or a new feature.
So part two can be (feature or fix).
Part three is your Issue name or task name.

### commit

Please use pre-commit before committing anything.

For setup pre-commit use this command:

``` pre-commit install ```

*Note*: Before using this command, ensure you installed the development requirements:

``` pip install -r requirements_dev.txt ```

If you forget to set up pre-commit before your commits in your machine, don't worry :D.
Use this command to fix your code with pre-commit:

``` pre-commit run --all-files ```

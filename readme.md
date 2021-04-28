# Djnago password-generator

### Generate strong password with
 - Numbers
 - Uppercase
 - Special Character

## Running Locally

```sh
$ git clone https://github.com/Vivek2509/password_generator.git
$ cd password_generator

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```
Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
# brycenall-site

## How to install

1. Clone the Django project
```sh
$ git clone https://github.com/crimsonslate/brycenall-site
```
2. Change into the brycenall-site directory
```sh
$ cd brycenall-site/
```
3. Create a Python virtual environment
```sh
$ python -m venv .venv
```
4. Activate the newly created virtual environment
```sh
$ source .venv/bin/activate
```
5. Install the Django project dependencies
```sh
(.venv)$ pip install -r requirements.txt
```
6. Make migrations for the `portfolio` app in your local database
```sh
(.venv)$ python manage.py makemigrations portfolio
```
7. Migrate your local database
```sh
(.venv)$ python manage.py migrate
```
8. Run the development server, served at `http://127.0.0.1:8000/` [Link](http://127.0.0.1:8000/)
```sh
(.venv)$ python manage.py runserver
```

I recommend creating a Django `superuser` afterward to access the Django admin:
```sh
(.venv)$ python manage.py createsuperuser
```
Then login [at admin/](http://127.0.0.1:8000/admin/) using that new user.

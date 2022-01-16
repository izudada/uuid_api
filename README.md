The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/uuid_api.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

Run the below command to effect database model migrations:
```sh
(folder_name)$ python manage.py migrate
```

Start the app with:
```sh
(folder_name)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
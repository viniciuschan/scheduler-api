# API REST that represents a scheduling system

Author: Vinícius Chan


## Prerequisites

* [Python3](https://www.python.org/download/releases/3.0/)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Django 1.11](https://docs.djangoproject.com/en/2.0/releases/1.11/)
* [Django Rest Framework](http://www.django-rest-framework.org)


### Getting Started

Install all dependencies:

```
pip install -r requirements.txt
```

Migrate:

```
python manage.py migrate
```

Run server:

```
python manage.py runserver
````


### Resources

List:
```
http://localhost:8000/appointments/
```
Detail:
```
http://localhost:8000/appointments/{id}/
````
Create:
```
http://localhost:8000/appointments/
```
Update:
```
http://localhost:8000/appointments/{id}/
```
Delete:
```
http://localhost:8000/appointments/{id}/
```
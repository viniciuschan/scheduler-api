# API REST that represents a scheduling system

Author: Vinícius Chan


## Requirements

* [Python3](https://www.python.org/download/releases/3.0/)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Django 1.11](https://docs.djangoproject.com/en/2.0/releases/1.11/)
* [Django Rest Framework 3](http://www.django-rest-framework.org)


### Getting Started

Activate virtualenv:

```
$ source <path>/bin/activate
```

Install all dependencies on virtualenv:

```
$ pip install -r requirements.txt
```

Migrate:

```
$ python manage.py migrate
```

Run server:

```
$ python manage.py runserver
````

Run tests:
```
$ python manage.py test -v2
```

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

## All the unit tests of the endpoints can be performed from my POSTMAN collection. Please, check it. =)
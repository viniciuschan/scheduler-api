# API REST that represents a scheduling system

Author: Vinícius Chan


## Requirements

* [Python 3.6.8](https://www.python.org/downloads/release/python-368/)
* [Django 1.11](https://docs.djangoproject.com/en/2.0/releases/1.11/)
* [Django Rest Framework 3.7.3](http://www.django-rest-framework.org)
* [Docker](https://www.docker.com/)
* [Docker-Compose](https://docs.docker.com/compose/)


### Getting Started

1. Run server:

```
$ make run
````

2. Migrate:

```
$ make migrate
```

3. Run tests:
```
$ make test
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

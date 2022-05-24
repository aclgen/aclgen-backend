# aclgen-backend

This is the REST API for the ACLGen web application.

## Running Django

* To run the Django backend, run:
``python manage.py runserver``

* To migrate new model changes to the database, run: ``python manage.py migrate [api]`` (replace api with other packages if necessary)

* To run tests, run: ``pytest``

## Swagger

Swagger is available on: http://localhost:8000/swagger/
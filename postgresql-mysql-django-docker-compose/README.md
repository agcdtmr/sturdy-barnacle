# Setting up PostgreSQL with Django App using Docker Compose

## Getting Started

- Clone the [repo](https://github.com/agcdtmr/sturdy-barnacle)
- `cd sturdy-barnacle/postgresql-mysql-django-docker-compose`
- Follow the [documentation](https://anj.hashnode.dev/setting-up-postgresql-with-django-app-using-docker-compose)


## ToDos

- [x] [Build and start a Django project with Docker Compose](https://www.youtube.com/watch?v=aMqs_y6dZw4&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=2&pp=iAQB)
- [x] Write a documentation
- [x] Edit cover image

## Error and Solution

1. 
```
ERROR: Could not find a version that satisfies the requirement pyscopg2-binary>=2.9.9 (from versions: none)
2.371 ERROR: No matching distribution found for pyscopg2-binary>=2.9.9
------
failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 1
```

#### Solution:
- Issue: The error indicates that the required version of psycopg2-binary is not available.
- Resolution: Check for the latest available version of psycopg2-binary.
- Recommended Action: Use psycopg2-binary>=2.9 instead of psycopg2-binary>=2.9.9 in your requirements file to ensure compatibility.

## Questions

- What is yaml?
- why 0.0.0.0 and not 127.0.0.1?
- At yaml file, there's a "depends_on: - db". If I run the yaml file without it, it doesn't create and run the db file/container. Why is that?
- depends on doesn't connect the containers together right? to connect the db to my django app, I need to adjust the settings.py DATABASES config
- How do you know if the app and db are connected? If we can apply the migrations, we can run the database.
- How to do the migrations? Use `docker exec -it <containerName> /bin/bash` and run `python manage.py migrate`
- [what does " python manage.py migrate " in django do exactly?](https://stackoverflow.com/questions/62311073/what-does-python-manage-py-migrate-in-django-do-exactly)
- Why postgres needs psycopg2-binary
- Database setting.py ----'ENGINE': 'django.db.backends.postgresql'
- What is Django and db migrations?


## Resources

- [docker-django-postgres .gitignore](https://github.com/martingstall/docker-django-postgres/blob/master/.gitignore)

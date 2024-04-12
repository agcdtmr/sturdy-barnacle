# sturdy-barnacle

## How to run

- cd sturdy-barnacle
- python3 -m venv <name>
- source <name>/bin/activate
- cat requirements.txt or pip freeze > requirements.txt
- python manage.py runserver

To build and run the container:
- docker build -tag python-django-app . 
- docker run -it -publish 8000:8000 python-django-app


http://127.0.0.1:8000
http://localhost:8000


## Creating a Django project

- [ ] Dockerize a Django application [Beginners Guide](https://www.youtube.com/watch?v=W5Ov0H7E_o4&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=1)
- [ ] Write a documentation inspired by this [blog](https://dockerize.io/guides/python-django-guide)

## Errors

1. 
`django-admin startproject mysite
zsh: command not found: django-admin`

django-admin command is not recognized, which typically means Django might not be installed or its binaries are not in your system's PATH.

If you've already installed Django using pip, you might need to ensure that the path to Django's binaries is included in your system's PATH environment variable.
`pip install django`


2.
```
Dockerfile:16
--------------------
  14 |     
  15 |     # This will install the packages we have in the requirements.txt file
  16 | >>> RUN pip install --no-cache-dir -r requirements.txt
  17 |     
  18 |     COPY . /app/
--------------------
ERROR: failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 1
```


3.
```
=> ERROR [6/7] RUN pip install --no-cache-dir -r requirements.txt                                                    0.8s
------                                                                                                                     
 > [6/7] RUN pip install --no-cache-dir -r requirements.txt:                                                               
0.630 Processing /private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_71xswk40o_/croot/aiobotocore_1682537536268/work                                                                                                                         
0.632 ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: '/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_71xswk40o_/croot/aiobotocore_1682537536268/work'
0.632 
0.735 
0.735 [notice] A new release of pip is available: 23.0.1 -> 24.0
0.735 [notice] To update, run: pip install --upgrade pip
------
Dockerfile:28
--------------------
  26 |     
  27 |     # Install Python dependencies inside the virtual environment
  28 | >>> RUN pip install --no-cache-dir -r requirements.txt
  29 |     
  30 |     # Copy the application code into the container
--------------------
ERROR: failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 1

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/x1rlvt5vc61l5hz58zrv6viwj
```


Solution:
- For 2 & 3 errors, I found out that I forgot to use the venv environment from the start.

4. 
```
docker run -it -p 8000:8000 python-django-app
Traceback (most recent call last):
  File "/app/manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/app/manage.py", line 22, in <module>
    main()
  File "/app/manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```

Solution:
- After solving the venv error. To solve this make sure you are at your venv then rerun `pip freeze > requirements.txt`

## Questions

- I've installed Python 12, now I have two Python files
- Why I need to run `python manage.py migrate`
- Is this state like in terraform?

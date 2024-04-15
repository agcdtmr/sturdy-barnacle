# Dockerize a Python Django App

## Getting Started

- Clone the [repo](https://github.com/agcdtmr/sturdy-barnacle)
- `cd sturdy-barnacle/dockerize-django-app`
- First, setup your Python virtual env locally. See the [documentation](https://anj.hashnode.dev/dockerize-a-python-django-app) how to do that.
- Build and running the container
`
$ cd <dockerize-django-app name>
$ docker build -tag <python-django-app or containerName> . 
$ docker run -it -p 8000:8000 <python-django-app or containerName>
`

- To see what Docker containers are running on your system (with their IDs):
`$ docker ps -a`

- To stop your Docker container:
`$ docker stop container_id`


## ToDos: Creating a Django project

- [x] Dockerize a Django application [Beginners Guide](https://www.youtube.com/watch?v=W5Ov0H7E_o4&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=1)
- [x] Write a documentation inspired by this [blog](https://dockerize.io/guides/python-django-guide)
- [ ] Bonus 1: SSL certificate for HTTPS


## Errors and Solutions

1. 
`django-admin startproject mysite
zsh: command not found: django-admin`

Error: When trying to start a Django project with `django-admin startproject core .`, the system shows zsh: command not found: django-admin. This usually happens when Django isn't installed in your local machine or its commands aren't in the system's PATH.

Solution: Install Django using pip install django. If Django is already installed, ensure its binaries are included in the system's PATH.


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

Error: While building a Docker image, the process fails at RUN pip install --no-cache-dir -r requirements.txt, showing an exit code 1.

Solution: This error often occurs when the virtual environment (venv) isn't used from the beginning.


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


Error: During Docker image build, the process fails with an OSError indicating a missing file or directory related to requirements.txt.

Solution: Similar to error 2, ensure the virtual environment (venv) is activated from the start.

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

Error: When running a Docker container with a Django application, an ImportError occurs stating No module named 'django'.

Solution: Activate the virtual environment (venv) before running the container. Ensure Django is installed within the virtual environment and rerun pip freeze > requirements.txt after resolving the venv issue.


## Questions while implementing this task

- I've installed Python 12, now I have two Python files
- Why I need to run `python manage.py migrate`
- Is this state like in terraform?

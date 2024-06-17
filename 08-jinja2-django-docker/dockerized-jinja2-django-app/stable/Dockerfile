# Use the official Python image for an Operating System
FROM python:3.12

# Ensure Python outputs everything that's printed inside the application
# Any errors logs sends straight to the terminal, we get the message straight away
# 1 means non empty value
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory in the container
WORKDIR /code

# copy requirements.txt from the local machine into the Docker container (/code/ directory)
COPY requirements.txt /code/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# # Copy the requirements file into the container
# COPY requirements.txt requirements.txt


# Use the official Python image for an Operating System
FROM python:3.12-alpine

# Ensure Python outputs everything that's printed inside the application
# Any errors logs sends straight to the terminal, we get the message straight away
# 1 means non empty value
# Info:
#     PYTHONUNBUFFERED:
#     Setting the non-empty value of PYTHONUNBUFFERED means 
#     that the python output is transmitted directly to the 
#     terminal without being buffered and that allows displaying 
#     the application’s output in real-time. 
ENV PYTHONUNBUFFERED=1

# This is just dependencies in order to get our PostgreSQL DB working on alpine
# This command updates the package index and installs necessary packages for developing with 
# PostgreSQL, including libraries and tools needed for compiling and running PostgreSQL-related code on an Alpine Linux system.
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Set working directory in the container
WORKDIR /django

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Upgrade pip
RUN pip install --upgrade pip
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
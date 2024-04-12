# Use the official Python image for an Operating System
FROM python:3.12

# Ensure Python outputs everything that's printed inside the application
# Any errors logs sends straight to the terminal, we get the message straight away
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /django

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

#
RUN pip install --upgrade pip
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

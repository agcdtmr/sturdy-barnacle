# Use the official Python image for an Operating System
FROM python:3.12-alpine

# Ensure Python outputs everything that's printed inside the application
# Any errors logs sends straight to the terminal, we get the message straight away
# 1 means non empty value
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Copy the all files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory in the container
WORKDIR /django

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


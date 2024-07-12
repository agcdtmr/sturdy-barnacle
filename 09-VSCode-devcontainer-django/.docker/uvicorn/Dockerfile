# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt before installing dependencies
COPY ../requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files into the working directory
COPY .. /app/

# Generate SSL certificates only in development
ARG DEV_ENV=false
RUN if [ "$DEV_ENV" = "true" ]; then \
        mkdir -p /etc/ssl && \
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/devcontainer.key -out /etc/ssl/devcontainer.crt -subj "/CN=localhost"; \
    fi
# Expose port 8000 for Uvicorn
EXPOSE 8000

# Default command to run the Django development server using Uvicorn
CMD ["uvicorn", "app.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

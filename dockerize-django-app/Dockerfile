# Use the official Python image for an Operating System
FROM python:3.12

# # Prevent Python from writing byte code
# ENV PYTHONDONTWRITEBYTECODE 1

# # Ensure Python outputs everything that's printed inside the application
# ENV PYTHONUNBUFFERED 1

# # Create a virtual environment
# RUN python -m venv /venv

# # Activate the virtual environment
# ENV PATH="/venv/bin:$PATH"

# Set working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# # Update package index and install Nano
# RUN apt-get update && apt-get install -y nano

#
RUN pip install --upgrade pip
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the all files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# "0.0.0.0:8000" makes the container externally available
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# - If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:
# `python manage.py runserver 8080`
    
# - If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
# `python manage.py runserver 0.0.0.0:8000`
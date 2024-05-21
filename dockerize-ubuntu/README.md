# Containerized Ubuntu Setup using Docker

This documentation provides detailed steps on how to set up a containerized Ubuntu environment using Docker. The repository already includes a `Dockerfile` and a `docker-compose.yaml` file. You'll just need to clone the repository and create a `.env` file for setting User ID (UID) and Group ID (GID) to ensure the container runs with the appropriate permissions.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository link>
cd dockerize-ubuntu
```

## Step 2: Create a .env File

Create a `.env` file in the root of the cloned repository with the following content:

```env
UID=2000
GID=2001
```

Adjust the `UID` and `GID` values to match your user and group ID on the host system. You can find your UID and GID by running:

```bash
id -u
id -g
```

## Step 3: Review the Dockerfile

The `Dockerfile` included in the repository should look like this:

```Dockerfile
# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:latest

# Add this line when necessary
# Set environment variables for non-interactive apt-get
# ENV DEBIAN_FRONTEND=noninteractive

# Define build arguments
ARG USER=user
ARG UID
ARG GID

# Set environment variables
ENV USER=$USER
ENV UID=$UID
ENV GID=$GID

# Install sudo and any necessary dependencies
RUN apt-get update && \
    apt-get install -y sudo \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with sudo privileges
RUN groupadd -g $GID $USER && \
    useradd -m -u $UID -g $GID -s /bin/bash $USER && \
    usermod -aG sudo $USER && \
    echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set the default user
USER $USER

# Set the default command to run when the container starts
CMD ["bash"]
```

## Step 4: Review the docker-compose.yaml

The `docker-compose.yaml` file included in the repository should look like this:

```yaml
version: '3'

services:
  ubuntu_container:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        UID: ${UID}
        GID: ${GID}
    tty: true
    stdin_open: true
    environment:
      - UID=${UID}
      - GID=${GID}
```

## Step 5: Build and Run the Docker Container

Use Docker Compose to build and run the container:

```bash
docker-compose up --build
```

This command will use the `UID` and `GID` from the `.env` file to build the Docker image and run the container.

## Summary of Commands

Here is a summary of the commands to set up and run the containerized Ubuntu:

1. **Clone the Repository:**
    ```bash
    git clone <repository link>
    cd ubuntu-docker
    ```

2. **Create `.env` File:**
    ```env
    UID=2000
    GID=2001
    ```

3. **Build and Run the Docker Container:**
    ```bash
    docker-compose up --build
    ```

## Additional Notes

- The `Dockerfile` uses `sudo` to allow the created user to execute commands with elevated privileges within the container. This is helpful for development and testing purposes but should be handled with care in a production environment.
- The `tty: true` option in `docker-compose.yaml` keeps the container running interactively, which is useful for development.

By following these steps, you can easily set up a containerized Ubuntu environment using Docker, with configurable user and group IDs for proper permissions.

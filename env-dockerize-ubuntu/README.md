# Containerized Ubuntu Setup using Docker for Development and Production Environments

This documentation provides detailed steps on how to set up a containerized Ubuntu environment using Docker for both development and production environments. 

The repository includes a:
- Dockerfile.dev
- Dockerfile.prod
- docker-compose.dev.yaml
- docker-compose.prod.yaml

You'll just need to clone the repository and create a .env file for setting User ID (UID) and Group ID (GID) to ensure the container runs with the appropriate permissions.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository link>
cd <root directory name>
```

## Step 2: Create a .env File

Create a `.env` file in the root of the cloned repository with the following sample content:

```env
UID=1000
GID=1000
```

Adjust the `UID` and `GID` values to match your user and group ID on the host system. You can find your UID and GID by running:

```bash
id -u
id -g
```

## Step 3: Review the Dockerfiles

- [ ] Development Dockerfile
- [ ] Production Dockerfile

## Step 4: Review the docker-compose Files

- [ ] Development `docker-compose.dev.yaml`
- [ ] Production `docker-compose.prod.yaml`

## Step 5: Build and Run the Docker Containers

### For Development

Use Docker Compose to build and run the container for development:

```bash
docker-compose -f docker-compose.dev.yaml up --build
```

### For Production

Use Docker Compose to build and run the container for production:

```bash
docker-compose -f docker-compose.prod.yaml up --build -d
```

## Important Notes

- The `Dockerfile.dev` includes additional packages like `vim` which can be useful during development.
- The `docker-compose.dev.yaml` mounts the current directory into the container, enabling live code editing.
- The `docker-compose.prod.yaml` is optimized for production with a restart policy to ensure the container runs continuously.

### Dockerfile Differences

#### Development (Dockerfile.dev):
- Additional Tools: Includes extra tools that are useful for development but not necessary in production. For example, vim is included for editing files directly within the container.
- Flexibility: The environment is more flexible to accommodate changes, debugging, and interactive sessions.

#### Production (Dockerfile.prod):
- Minimal Tools: Includes only the necessary tools to keep the image size small and reduce potential security vulnerabilities.
- Optimization: Focuses on performance and stability, without unnecessary packages or tools.


### Docker Compose Differences

#### Development (docker-compose.dev.yaml):
- Volume Mounting: Mounts the current directory into the container, allowing for live code editing and immediate reflection of changes.
- Port Mapping: Maps necessary ports to facilitate access to development services.
- Interactive Mode: Keeps the container running interactively (tty: true), which is useful for debugging and development.

#### Production (docker-compose.prod.yaml):
- No Volume Mounting: Does not mount directories from the host to avoid unintended changes and security risks.
- Restart Policy: Includes a restart policy (restart: unless-stopped) to ensure the container automatically restarts if it crashes, enhancing reliability.
- Detached Mode: `docker-compose -f docker-compose.prod.yaml up --build -d` Typically runs in detached mode (-d), meaning it runs in the background without tying up the terminal.

By following these steps, you can easily set up a containerized Ubuntu environment using Docker for both **development** and **production**, with configurable user and group IDs for proper permissions.


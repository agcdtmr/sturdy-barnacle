# VSCode Dev Container setup with django, pg, celery, valkey and rmq

## Terminologies
- pg: PostgreSQL
- celery: [Celery](https://docs.celeryq.dev/en/stable/index.html)
- valkey: [Valkey](https://valkey.io/)
- rmq: RabbitMQ


### Devcontainer Setup Summary

This VSCode dev container setup for a django, pg, celery, valkey and rmq project includes the following configurations and components:

1. **Configuration Files**: 
   - `devcontainer.json` is the primary configuration file.
   - **Initialize Command**: Copies `.devcontainer/.env.dev` to `.env` for environment setup.

2. **Docker and Docker Compose**:
   - Uses `../docker-compose.yml` to define and run the multi-container application.
   - At `/.docker/uvicorn/Dockerfile`, it sets the default command to run the Django development server using Uvicorn and generates SSL Certificates for development environment



6. **VSCode Customizations**:
   - **Extensions**:
     - Django-related extensions for HTML, IntelliSense, and general support.
     - Python extensions for linting and code analysis.
     - Docker extension for container management.
     - GitLab extension for workflow integration.
   - **Settings**:
     - Sets the Python interpreter path to `/usr/local/bin/python`.

7. **Development Features**:
   - Git, Python, Bash commands, Devcontainers CLI, Homebrew package management, Prettier, Pylint, Zsh plugins, and Jira CLI are included.

8. **Port Forwarding**:
   - Forwards necessary ports for development:
     - `8000`: Django
     - `5432`: PostgreSQL
     - `6379`: Valkey
     - `5672`: RabbitMQ (AMQP)
     - `15672`: RabbitMQ Management UI

### Additional Setup Details

- **Environment Setup**:
  - Initializes the environment by copying the environment configuration file.
- **Database Migrations**:
  - Runs necessary migrations to set up the database schema after container creation.

This setup ensures a consistent development environment with all necessary tools, extensions, and configurations pre-installed and ready to use.

# Setup of a Django project with pg, celery, valkey and rmq using VSCode dev containers and docker compose

To use the repository follow these steps:

### Setup Instructions

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/agcdtmr/sturdy-barnacle/tree/main
   cd sturdy-barnacle/09-VSCode-devcontainer-django
   ```

2. **Open in VSCode**:
   - Ensure Docker is installed and running.
   - Open the repository in VSCode.
   - If prompted, reopen the folder in the dev container. VSCode should recognize the `devcontainer.json` and suggest reopening in the container.

6. **Verify Connections**:
   - Once Dev Container setup is successfully done, verify the connections:
     - **PostgreSQL**: Check if PostgreSQL is running and accessible from your Django application. You can use tools like `psql` or connect directly from Django using the configured database settings.
     - **RabbitMQ**: Access the RabbitMQ Management UI at `http://localhost:15672`. Check [.env](https://github.com/agcdtmr/sturdy-barnacle/blob/main/09-VSCode-devcontainer-django/.devcontainer/.env.dev) file for default username and password.

### Testing Successful Connections

To ensure that the containers are successfully connected and your Django project is working as expected:

1. **Access Django Application**:
   - Open your web browser and navigate to `http://localhost:8000` to access your Django application.
   - If you configured SSL and generated SSL certificates, use `https://localhost:8000`.

2. **Database Connection**:
   - Verify that Django can connect to PostgreSQL. Check the terminal output for any database migration errors (`python manage.py migrate`) during the Docker Compose startup.
   - You can also connect to PostgreSQL using `psql` or a database management tool to ensure the database is populated with your application data.

3. **RabbitMQ Integration**:
   - Ensure Celery tasks are working by running a test task and monitoring its execution via the RabbitMQ Management UI (`http://localhost:15672`).

4. **Valkey Integration**:
   - Test integration with Valkey by executing and verifying functionality within your Django application that interacts with Valkey's services.

### Additional Tips

- **Debugging**: Use VSCode's debugging tools to set breakpoints and debug your Django application running inside the Docker container.
- **Logging**: Monitor Docker container logs (`docker-compose logs`) for any errors or issues that might occur during startup or operation.
- **Environment Variables**: Ensure all necessary environment variables are correctly set in your `devcontainer.json` and `.env` files for local development.

By following these steps, you should be able to set up and test your Django project with PostgreSQL, Celery, Valkey, and RabbitMQ using VSCode Dev Containers and Docker Compose effectively.

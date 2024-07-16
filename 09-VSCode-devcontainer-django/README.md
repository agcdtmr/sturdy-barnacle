# Setup of a Django project with pg, celery, valkey and rmq using VSCode dev containers and docker compose

### Terminologies
- pg: PostgreSQL
- celery: [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
- valkey: [Valkey](https://valkey.io/)
- rmq: RabbitMQ

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
   To ensure successful integration with Valkey within your Django project setup using VSCode Dev Containers and Docker Compose, try out these tests:

4.1. **Access Valkey Container Terminal**:
   - Open a terminal session inside the Valkey container to interact directly with its environment.
     ```sh
     docker exec -it <valkey-container-id> bash
     ```
   - Replace `<valkey-container-id>` with the actual container ID or name of the Valkey container.

4.2. **Basic Connectivity Tests**:
   - **Ping Test**:
     - From within the Valkey container, attempt to ping other containers or services (e.g., PostgreSQL, RabbitMQ) to verify network connectivity:
       ```sh
       ping <container-name>
       ```
       - Replace `<container-name>` with the name or IP address of the container you want to ping (e.g., `postgres`, `rabbitmq`).

3. **Service Endpoint Access**:
   - Verify that Valkey can access the endpoints of other services:
     - **PostgreSQL**:
       - Connect to PostgreSQL from the Valkey container using tools like `psql`:
         ```sh
         psql -h <postgres-container-name> -U <postgres-user> <database-name>
         ```
         - Replace `<postgres-container-name>`, `<postgres-user>`, and `<database-name>` with your PostgreSQL container name, username, and database name.
     - **RabbitMQ**:
       - Ensure Valkey can interact with RabbitMQ's AMQP endpoint. You can check connectivity and queue operations from the Valkey container.

4. **Monitor Logs**:
   - Monitor Valkey container logs (`docker logs <valkey-container-id>`) for any errors or issues that may occur during integration tests. Ensure all logs are captured and reviewed for debugging purposes.

#### Example Workflow

Here's an example workflow to test Valkey integration:

1. Access Valkey container terminal:
   ```sh
   docker exec -it <valkey-container-id> bash
   ```

2. Perform ping test:
   ```sh
   ping postgres
   ```

3. Connect to PostgreSQL from Valkey container:
   ```sh
   psql -h postgres -U postgres
   ```

By following the examples above, you can ensure that Valkey is properly integrated and functioning within your Django project's development environment using VSCode Dev Containers and Docker Compose. Adjust tests and configurations as needed based on your specific application requirements and Valkey's capabilities.

### Additional Tips

- **Debugging**: Use VSCode's debugging tools to set breakpoints and debug your Django application running inside the Docker container.
- **Logging**: Monitor Docker container logs (`docker-compose logs`) for any errors or issues that might occur during startup or operation.
- **Environment Variables**: Ensure all necessary environment variables are correctly set in your `devcontainer.json` and `.env` files for local development.

Congratulations! You've successfully configured and tested your Django project with PostgreSQL, Celery, Valkey, and RabbitMQ using VSCode Dev Containers and Docker Compose. Now, you can proceed with app development and collaborate seamlessly with your team. Happy coding!

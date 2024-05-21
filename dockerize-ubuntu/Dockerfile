# Use the official Ubuntu base image
FROM ubuntu:latest

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

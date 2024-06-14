# Dockerfile
FROM valkey/valkey

# Copy the configuration files
COPY valkey.conf /etc/valkey/valkey.conf
COPY valkey.acl /etc/valkey/valkey.acl

# Expose the port Valkey runs on (example: 6379 for Redis)
EXPOSE 6379

# Start Valkey server (replace with the correct start command if different)
CMD ["valkey-server", "/etc/valkey/valkey.conf"]

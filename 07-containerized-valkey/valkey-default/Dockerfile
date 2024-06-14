# Use the official Valkey base image
FROM valkey/valkey

# Copy your custom configuration file into the container
# COPY valkey.conf /usr/local/etc/valkey/valkey.conf
# COPY above this commented because it cause ERROR: 
# ERROR [valkey 2/2] COPY valkey.conf /usr/local/etc/valkey/valkey.conf                                             0.0s
# ------
#     > [valkey 2/2] COPY valkey.conf /usr/local/etc/valkey/valkey.conf:
#    ------
#    failed to solve: failed to compute cache key: failed to calculate checksum of ref eba28416-fd16-41a4-aef0-f2e650eac68b::u2z82towcvrhonmrqzumcho6y: "/valkey.conf": not found
# Since you're using an existing base image (valkey/valkey) and the configuration file is mounted via a volume in Docker Compose, there's no need to copy the configuration file in the Dockerfile. This simplifies your Dockerfile significantly




# Run the Valkey server with your custom configuration file
CMD ["valkey-server", "/usr/local/etc/valkey/valkey.conf"]

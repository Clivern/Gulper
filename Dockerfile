# Use Ubuntu as the base image
FROM ubuntu:24.04

# Update the package index
RUN apt update

# Install MySQL and PostgreSQL client tools
RUN apt install -y mysql-client postgresql-client python3-pip

# Install dumpitt
RUN pip3 install dumpitt

# Verify the installation of mysqldump and pg_dump and dumpitt
RUN mysqldump --version
RUN pg_dump --version
RUN dumpitt --version

# Set the working directory
WORKDIR /app

COPY config.yaml /app/config.yaml

CMD ["dumpitt", "--config", "/app/config.yaml"]

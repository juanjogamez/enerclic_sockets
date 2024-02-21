# Automated Client-Server System (enerclic-sockets)

## Overview
This repository aims to implement automation for establishing a client-server-client system. Both clients can exchange messages with each other through the server. The server and client are implemented in Python in the files `server.py` and `client.py`, respectively. For ease of use, Dockerization has been opted for. Given the illustrative purposes of this repository, two Dockerfiles (`/docker/df_client` and `/docker/df_server`) have been established. Both, starting from an Alpine image, will generate an image with the required Python file (server or client) and with Python3 installed for subsequent execution. These Dockerfiles are included in `docker-compose.yml` (build section of each service (container)). Additionally, in the same `docker-compose.yml`, the necessary Docker Network configuration is established as well as the necessary volumes and entry commands.

## Requirements
- Docker
- Docker Compose

## Installation and Usage
1. Edit the `docker-compose.yml` file, specifying the local path to be linked as a volume (`/home/juanjogamez/enerclic_sockets/logs/server`) with the resulting path after cloning this repository.
2. In the `enerclic_sockets/` directory, run `docker-compose up`.
3. Three Docker containers (one server and two clients) will be automatically running.
4. Access each of the client-relative containers via `docker exec -it container_id sh` and execute the client's Python code (`python3 /app/client.py`).
5. Both clients should be interconnected through the server.
6. Locally, you can check the message logs in the file `/localpath/enerclic_sockets/logs/server/messages.log`.

## References
- [Python Socket Library Documentation](https://docs.python.org/3/library/socket.html)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
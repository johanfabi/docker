# Ubuntu Shell Docker Container

This repository contains a Dockerfile for creating a Docker container with Ubuntu and bash installed. This container is designed for practicing shell scripting.

## Building the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```bash
docker build -t ubuntu-shell .
```

## Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -d --name ubuntu-shell ubuntu-shell
```

## Accessing the Container

To access the container, use the following command:

```bash
docker exec -it <container_id> bash
```



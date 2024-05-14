# Ollama Models - Docker

This is a simple example of how to use Ollama Models into Docker.

## Docker Containers

1. Run the Docker container with the following command:

```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

2. Open your browser and navigate to `http://localhost:11434` to see the Ollama IA.

3. If you want to run a Ollama IA into the container, use de following command:
```
docker exec -it ollama ollama --help
```

## Run with Docker Compose

1. Run the Docker container with the following command:

```
docker-compose up -d
```

## Install Models

1. If you want to install a model into the container, use de following command.

```
docker exec -it ollama ollama run <model>
```

Example:

```
docker exec -it ollama ollama run qwen:0.5b
```

Ollama Models are available at https://ollama.com/library

## Send a request to the Ollama IA

1. Edit the main.py file with your own content.



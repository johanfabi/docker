# NGINX - Docker

This is a simple example of how to use NGINX into Docker.

## How to use

1. Clone this repository.

2. Replace the `src/index.html` file with your own content.

3. Build the Docker image with the following command:
```bash
docker build -t docker-nginx .
```
4. Run the Docker container with the following command:
```bash
docker run -d --name docker-nginx -p 8080:80 docker-nginx
```
5. Open your browser and navigate to `http://localhost:8080` to see your content.


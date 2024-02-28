# Docker Terraform

This is a simple example of how to use Terraform into Docker.

## How to use
1. Clone this repository.
2. Build the Docker image with the following command:
```bash
docker build --build-arg PRODUCT=terraform --build-arg VERSION=1.7.4 -t docker-terraform .
```
3. Run the Docker container with the following command:
```bash
docker run -it docker-terraform terraform -help
```

## Terraform releases
You can find all Terraform releases at [https://releases.hashicorp.com/terraform/](https://releases.hashicorp.com/terraform/).




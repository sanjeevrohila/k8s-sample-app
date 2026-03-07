# Flask Docker Application

This repository contains a simple **Flask web application packaged inside a Docker image**.  
It demonstrates how to build, run, and publish a containerized application using Docker.

---

## Docker Images

Two different versions of Docker images are published from this repository:

- `justsanjeev/application:v1`
- `justsanjeev/application:v2`

Docker Hub Repository:

https://hub.docker.com/repository/docker/justsanjeev/application

---

## Run the Application

Pull the Docker image:

```bash
docker pull justsanjeev/application:v1
```

Run the container:

```bash
docker run -p 3000:3000 justsanjeev/application:v1
```

Open the application in your browser:

```
http://localhost:3000
```

---

## Build the Docker Image

To build the Docker image locally:

```bash
docker build -t justsanjeev/application:v1 .
```

---

## Push the Image to Docker Hub

After building the image, push it to Docker Hub:

```bash
docker push justsanjeev/application:v1
```

---

## Project Purpose

This project demonstrates:

- Creating a simple Flask web application
- Packaging the application inside a Docker container
- Publishing Docker images to Docker Hub
- Running the application using Docker

---

## Technologies Used

- Python
- Flask
- Docker

---

## Author

**Sanjeev**

DockerHub:  
https://hub.docker.com/u/justsanjeev

# Flask Docker Application

This repository contains a simple **Flask web application packaged inside a Docker image**.  
It demonstrates how to build, run, and publish a containerized application using Docker and
exploye different deployment strategies.

---

## Docker Images

Two different versions of Docker images are published from this repository:

- `docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v1 --push .`
- `docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v2 --push .`
  

Docker Hub Repository:

https://hub.docker.com/repository/docker/justsanjeev/application

---

## Run the Application

Pull the Docker image:

```bash
docker pull justsanjeev/application-larch:v1
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

## Now create new images for Linux atchicture 
```bash
docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v1 --push .
docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v1 --push .

```


---

## Project Purpose

This project demonstrates:

- Creating a simple Flask web application
- Packaging the application inside a Docker container
- Publishing Docker images to Docker Hub
- Running the application using Docker
- Deploying and then change the deployment with new verson

---


## Create deployment, with RollingUpdates startegy with 3 replicas

```bash
~/simpleapp$ cat deployment.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
  labels:
    app: flask-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-container
        image: justsanjeev/application:v1
        ports:
        - containerPort: 3000
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
```

## Create service as well

```bash

:~/simpleapp$ cat service.yaml 
apiVersion: v1
kind: Service
metadata:
  name: flask-service

spec:
  type: NodePort

  selector:
    app: flask-app

  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 30007
```

## Explanation - Full Traffic Path

```bash
External User
     │
     │ http://NODE_IP:30007
     ▼
Kubernetes Node
     │
     │ NodePort (30007)
     ▼
Service
     │
     │ Service Port (80)
     ▼
Pod
     │
     │ Container Port (3000)
     ▼
Flask Application
```



## Technologies Used

- Python
- Flask
- Docker

---

## Author

**Sanjeev**

DockerHub:  
https://hub.docker.com/u/justsanjeev

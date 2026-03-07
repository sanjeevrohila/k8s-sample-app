# Flask Docker Application

This repository contains a simple **Flask web application packaged inside a Docker image**.  
It demonstrates how to:

- Build a containerized Python application
- Push Docker images to Docker Hub
- Deploy the application on Kubernetes
- Use a **RollingUpdate deployment strategy**
- Expose the application using a **NodePort service**

---

# Docker Images

Two different versions of Docker images are published from this repository.

### Build and Push Images

```bash
docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v1 --push .
docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v2 --push .
```

Docker Hub Repository:

https://hub.docker.com/repository/docker/justsanjeev/application

---

# Run the Application Using Docker

Pull the image from Docker Hub:

```bash
docker pull justsanjeev/application-larch:v1
```

Run the container:

```bash
docker run -p 3000:3000 justsanjeev/application-larch:v1
```

Open the application in your browser:

```
http://localhost:3000
```

---

# Build Docker Image Locally

```bash
docker build -t justsanjeev/application-larch:v1 .
```

---

# Push Image to Docker Hub

```bash
docker push justsanjeev/application-larch:v1
```

---

# Project Purpose

This project demonstrates:

- Creating a simple Flask web application
- Packaging the application inside a Docker container
- Publishing Docker images to Docker Hub
- Running containers locally
- Deploying the application on Kubernetes
- Updating the deployment using new image versions

---

# Kubernetes Deployment

A **Deployment** is created with **3 replicas** and a **RollingUpdate strategy**.

```yaml
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
        image: justsanjeev/application-larch:v1

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

Apply the deployment:

```bash
kubectl apply -f deployment.yaml
```

---

# Kubernetes Service

A **NodePort service** exposes the application outside the cluster.

```yaml
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

Apply the service:

```bash
kubectl apply -f service.yaml
```

---

# Service Port Explanation

```yaml
ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
    nodePort: 30007
```

| Field | Description |
|------|-------------|
| protocol | Network protocol used (TCP) |
| port | Service port inside the Kubernetes cluster |
| targetPort | Port where the container application listens |
| nodePort | External port exposed on every Kubernetes node |

---

# Full Traffic Flow

```
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

---

# Verify Kubernetes Resources

### Check Pods

```bash
kubectl get pods
```

Example:

```
flask-app-54bddcd89d-6l9bf   1/1 Running
flask-app-54bddcd89d-8695l   1/1 Running
flask-app-54bddcd89d-bft54   1/1 Running
```

---

### Check Endpoints

```bash
kubectl get endpoints flask-service
```

Example:

```
flask-service   192.168.86.8:3000
                192.168.86.9:3000
                192.168.91.206:3000
```

---

### Check Pods with Node Details

```bash
kubectl get pods -o wide
```

Example:

```
NAME                       READY STATUS  IP              NODE
flask-app-xxxxx            1/1   Running 192.168.91.206  ubuntu-worker1
flask-app-xxxxx            1/1   Running 192.168.86.8    ubuntu-worker2
flask-app-xxxxx            1/1   Running 192.168.86.9    ubuntu-worker2
```

---

# Access Application Using Port Forward

If NodePort is not accessible, use port-forwarding:

```bash
kubectl port-forward --address 0.0.0.0 svc/flask-service 8080:80
```

Access application:

```
http://localhost:8080
```





# create new APP version with code changes

```bash
docker buildx build --platform linux/amd64 -t justsanjeev/application-larch:v2 --push .
```



# And deploye the new verion

```bash
~/simpleapp$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
city-backend-7987544dd5-8rxcc   1/1     Running   0          28d
city-backend-7987544dd5-kj5vm   1/1     Running   0          28d
flask-app-54bddcd89d-6l9bf      1/1     Running   0          163m
flask-app-54bddcd89d-8695l      1/1     Running   0          163m
flask-app-54bddcd89d-bft54      1/1     Running   0          163m
postgres-0                      1/1     Running   0          28d
~/simpleapp$ 
:~/simpleapp$ kubectl set image deployment/flask-app-v2 flask-container=justsanjeev/application-larch:v2
Error from server (NotFound): deployments.apps "flask-app-v2" not found
~/simpleapp$ kubectl get deployment
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
city-backend   2/2     2            2           28d
flask-app      3/3     3            3           8h
~/simpleapp$ kubectl set image deployment/flask-app flask-container=justsanjeev/application-larch:v2
deployment.apps/flask-app image updated
:~/simpleapp$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
city-backend-7987544dd5-8rxcc   1/1     Running   0          28d
city-backend-7987544dd5-kj5vm   1/1     Running   0          28d
flask-app-c4dcffb45-nhvtq       1/1     Running   0          16s
flask-app-c4dcffb45-sqrs8       1/1     Running   0          19s
flask-app-c4dcffb45-wqwzq       1/1     Running   0          19s
postgres-0                      1/1     Running   0          28d

```
---

# Technologies Used

- Python
- Flask
- Docker
- Kubernetes

---

# Author

**Sanjeev**

DockerHub  
https://hub.docker.com/u/justsanjeev

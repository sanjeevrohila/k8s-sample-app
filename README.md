# k8s-sample-app
There are two different versions of images are posted from this repository 
justsanjeev/application:v2
justsanjeev/application:v1

Run It sith steps below 
docker pull justsanjeev/application:v1
docker run -p 3000:3000 justsanjeev/application:v1



Steps to build and push 
docker build -t justsanjeev/application:v1 .
docker push justsanjeev/application:v1

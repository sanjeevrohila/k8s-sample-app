from flask import Flask, render_template

app = Flask(__name__)

tech = [
    {"name":"Docker","img":"docker.png"},
    {"name":"Kubernetes","img":"kubernetes.png"},
    {"name":"Linux","img":"linux.png"},
    {"name":"Ubuntu","img":"ubuntu.png"},
    {"name":"RedHat","img":"redhat.png"},
    {"name":"Windows","img":"windows.png"},
    {"name":"MacOS","img":"macos.png"},
    {"name":"Python","img":"python.png"},
    {"name":"Respberry Pi","img":"respberrypi.png"},
    {"name":"Kafka","img":"kafka.png"},
    {"name":"Apache Airflow","img":"airflow.png"},
    {"name":"Centos","img":"centos.png"},
]

@app.route("/")
def home():
    return render_template("index.html", tech=tech)

@app.route("/health")
def health():
    return {"status":"running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000)

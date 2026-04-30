from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps CI/CD com Kubernetes funcionando!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/metrics")
def metrics():
    return "app_requests_total 1\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
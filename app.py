from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Project Running Successfully!"

@app.route("/health")
def health():
    return {
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "Memory Usage": f"{psutil.virtual_memory().percent}%"
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
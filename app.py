from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello DevOps World! My CI/CD pipeline is coming...</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
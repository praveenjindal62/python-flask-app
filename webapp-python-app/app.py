from flask import Flask
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def get_data():
    return requests.get('http://localhost:5100').content

if __name__ == "__main__":
    app.run(host="0.0.0.0")
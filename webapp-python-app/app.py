from flask import Flask
import requests
import os
app = Flask(__name__)
VM_URL = os.environ['VMAPP_URL']

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def get_data():
    return "<H1>" + requests.get(VM_URL).content + "</H1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
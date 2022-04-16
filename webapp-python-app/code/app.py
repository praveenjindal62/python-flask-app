from flask import Flask
import requests
import os
app = Flask(__name__)
VM_URL = os.environ.get('VMAPP_URL') 

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def get_data():
    if VM_URL == None:
        return "<H1>" + "APP URL Is not defined using env variable" + "</H1>"
    else:
        return "<H1>" + requests.get(VM_URL).content.decode("utf-8") + "</H1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from flask import Flask
import os
app = Flask(__name__)

content = os.getenv('VMAPP_CONTENT', 'VMApp Default Content')
@app.route('/')
def hello():
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0")
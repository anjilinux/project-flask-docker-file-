from flask import Flask,jsonify,request
from time import time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
        "message" : 'Hello World',
        "timestamp" : int(time()),
        }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
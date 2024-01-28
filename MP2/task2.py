from flask import Flask,jsonify, request
import subprocess
import socket



app = Flask(__name__)


@app.route('/', methods = ['GET']) 
def home(): 
    return str(socket.gethostname() )
    
@app.route('/', methods = ['POST']) 
def post():
    subprocess.Popen(['python3 stress.py'], shell=True)
    return str("0")
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0',port=80)
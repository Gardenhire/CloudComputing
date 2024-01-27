from flask import Flask,jsonify, request



app = Flask(__name__)

global seedNumber
seedNumber = '0'

@app.route('/', methods = ['GET']) 
def home(): 
    global seedNumber
    return str(seedNumber)
    
@app.route('/', methods = ['POST']) 
def post():
    global seedNumber
    content = request.get_json(silent=True)
    seedNumber = content['num']
    return str(seedNumber)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.',port=5000)
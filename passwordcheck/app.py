#
#
#
from flask import request, Flask
import json, socket


app = Flask(__name__)

#
# curl http://localhost:9001
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"password\" : \"xxxxxxxx\" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"
#
@app.route("/check", methods=["POST"])
def compute():

    nums_ = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    lower_ = {'a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z'}
    upper_ = {'A', 'B', 'C', 'D', 'E',
              'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z'}

    
    hostName = socket.gethostname()

    password = request.json['password']
    password_length = len(password)

    returnDictionary = {}
    returnDictionary["password"] = password
    returnDictionary["length"] = password_length
    returnDictionary["success"] = False

    
    has_num = has_lower = has_upper = False
    for c_ in password:

        if c_ in nums_: has_num = True
        if c_ in lower_: has_lower = True
        if c_ in upper_: has_upper = True

        if has_num and has_lower and has_upper: break
            
    if has_num and has_lower and has_upper and password_length >= 5: returnDictionary["success"] = True
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)

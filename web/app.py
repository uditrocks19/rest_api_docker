from flask import Flask,jsonify,request
from flask_restful import Api,Resource
app=Flask(__name__)
api=Api(app)

@app.route('/')

def hello_world():
    return "Hello World"

def checkPostedData(PostedData,function_name):
    if function_name in ("add","subtract","multiply"):
        if "x" not in PostedData or "y" not in PostedData:
            return 400
        else:
            return 200
    elif function_name=="divide":
        if "x" not in PostedData or "y" not in PostedData:
                return 400
        elif  int(PostedData["y"])==0:
                return 401
        else:
            return 200

class Add(Resource):
    def post(self):
        data=request.get_json()

        status_code=checkPostedData(data,"add")
        if status_code!=200:
            ret_json={
                "Message":"Some arguments were missing",
                "Status code":400
            }
            return jsonify(ret_json)
        x, y = int(data["x"]), int(data["y"])
        ret=x+y
        ret_json={
            "Message":ret,
            "Status Code":200

        }
        return jsonify(ret_json)


class Subtract(Resource):
    def post(self):
        data=request.get_json()

        status_code=checkPostedData(data,"subtract")
        if status_code!=200:
            ret_json={
                "Message":"Some arguments were missing",
                "Status code":status_code
            }
            return jsonify(ret_json)
        x, y = int(data["x"]), int(data["y"])
        ret=x-y
        ret_json={
            "Message":ret,
            "Status Code":200

        }
        return jsonify(ret_json)


class Multiply(Resource):
    def post(self):
        data=request.get_json()

        status_code=checkPostedData(data,"multiply")
        if status_code!=200:
            ret_json={
                "Message":"Some arguments were missing",
                "Status code":status_code
            }
            return jsonify(ret_json)
        x, y = int(data["x"]), int(data["y"])
        ret=x*y
        ret_json={
            "Message":ret,
            "Status Code":200

        }
        return jsonify(ret_json)


class Divide(Resource):
    def post(self):
        data=request.get_json()

        status_code=checkPostedData(data,"divide")
        if status_code!=200:
            if status_code==400:
                ret_json={
                "Message":"Some arguments were missing",
                "Status code":status_code
                }
                return jsonify(ret_json)
            elif status_code==401:
                ret_json = {
                    "Message": "y should not be zero",
                    "Status code":status_code
                            }
                return jsonify(ret_json)

        x, y = int(data["x"]), int(data["y"])
        ret=x/y
        ret_json={
            "Message":ret,
            "Status Code":200

        }
        return jsonify(ret_json)

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Divide,"/divide")
api.add_resource(Multiply,"/multiply")

@app.route('/add_two_numbers',methods=["POST"])

def add_two_numbers():
    #get x and y from the posted data
    #add x and y store it in and send  a response
    data=request.get_json()
    x=data["x"]
    y=data["y"]
    z=x+y
    ret={
        "Z":z
    }
    return jsonify(ret),200

@app.route('/udit')
def bye_world():
    ret={
        'Name':'Udit',
        'Class':'5'
        }
    return jsonify(ret)

if __name__=='__main__':
    app.run(debug=True)

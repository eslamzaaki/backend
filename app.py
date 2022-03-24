from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
from script.test import test1
from script.test2 import test2
import os
app = Flask(__name__)

    ### CORS section
@app.after_request
def after_request_func(response):
        origin = request.headers.get('Origin')
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
            response.headers.add('Access-Control-Allow-Methods',
                                'GET, POST, OPTIONS, PUT, PATCH, DELETE')
            if origin:
                response.headers.add('Access-Control-Allow-Origin', origin)
        else:
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            if origin:
                response.headers.add('Access-Control-Allow-Origin', origin)

        return response
    ### end CORS section

@app.route('/testscript',methods=["POST"])
def index():
        body = request.get_json()
        test_url = body.get('testurl')
        response=jsonify(test1(test_url))
        return response
 
    

@app.route('/testscript2',methods=["POST"])
def index2():
        body = request.get_json()
        password = body.get('password')
        message=test2(password)
        response=jsonify({'message':message})
        return response
@app.route('/uploadFile', methods=['POST'])
def upload_file():
    if request.files is not None:
          uploaded_file = request.files['File']
          if uploaded_file.filename != '':
              uploaded_file.save(os.path.join("./files",uploaded_file.filename))
              return jsonify({'message':'success'})
    else:
        return jsonify({"message":"nofile"})            

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
#password of cf account => Eslam123#
##Deploy Back end
 #must be requirements.txt and Procfile
 #step 1 => cf api <api>
 #step 2 => cf login or cf login --sso
 #step 3 =>  cf push testscript -b https://github.com/cloudfoundry/python-buildpack.git

#front end 
 #cf push fronttes
 #npm install
 #npm build 
 #create mainfest.yml
 #empty file in /build with name Staticfile
 
#front end link => https://fronttest.cfapps.ap21.hana.ondemand.com/
#back end link => testscript-boisterous-possum-kx.cfapps.ap21.hana.ondemand.com 
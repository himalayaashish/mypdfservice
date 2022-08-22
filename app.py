from flask import Flask, request
import requests
import test
import time
import json
from flask import jsonify


app = Flask(__name__)
result = {}
@app.route('/', methods=['GET','POST'])
def post_route():
    if request.method == 'POST':

        data = request.get_json(force=True)

        #print('Data Received: "{data}"'.format(data=data))
        new_data = data
        response = requests.get(new_data['foo'])
        filename = "ABC.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        time.sleep(10)
        test.test_pdf(filename)
        with open('data.json', "r") as file:
            data_dict = json.load(file)
        result['data'] =data_dict
        return jsonify(result)



if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host="127.0.1.1", port=8080, debug=True)


#https://workdrive.zohoexternal.com/external/5ddc030e96a492cee1cf7beb3a3d0c75686bb389078183446eddbbe49afd2d24/download?directDownload=true

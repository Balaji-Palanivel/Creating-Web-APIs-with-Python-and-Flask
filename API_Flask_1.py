
import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def api_all():
    f = open("sample.json","r")
    author = f.read()
    authors = json.loads(author)
    return authors


@app.route('/api/add', methods=['POST'])
def api_id():
    req = request.get_json()
    f = open("sample.json","r")    
    author = f.read()
    authors = json.loads(author)
    authors.append({"Id_number" : req['id']})
    f.close()  
    file = open("sample.json","w")
    file.write(json.dumps(authors))
    file.close()
    return authors



app.run()
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def hello_world():
    return 'This is my first API call!'


@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True)
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)

@app.route('/test',methods=["GET","POST"])
def test():
    if request.method=='GET':
        return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

    elif request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")

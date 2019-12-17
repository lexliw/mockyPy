from flask import Flask, escape, request

app = Flask(__name__)

#GET simples
@app.route('/',methods = ['GET'])
def hello():
    resp = """
    {
        "name": "%s",
        "instructions": "%s",
        "teste": "%s"
    }
    """
    resp = resp % ('José da Silva', 'superior', 'ok')
    return resp, 200, {'Content-Type': 'application/json; charset=utf-8'}

#GET com path param
@app.route('/ids/<id>',methods = ['GET'])
def id(id):
    resp = """
    {
        "id": "%s",
        "name": "%s",
        "detail": "%s"
    }
    """
    resp = resp % (id, 'MaLu', 'color hair')
    return resp, 200, {'Content-Type': 'application/json; charset=utf-8'}

#GET com query param
@app.route('/search',methods = ['GET'])
def search():
    user = request.args.get('user')
    name = request.args.get('name')
    resp = """
    {
        "id": "%s",
        "user": "%s",
        "name": "%s"
    }
    """
    resp = resp % ('112233', user, name)
    return resp, 200, {'Content-Type': 'application/json; charset=utf-8'}

#POST simples
@app.route('/newid',methods = ['POST'])
def newid():
    req = request.json

    id = req['id']
    name = req['name']
    job = req['detail']['job']
    hobby = req['detail']['hobby']
    message = 'Salvo com Sucesso!!!'

    resp = """
    {
        "id": "%s",
        "name": "%s",
        "detail":{
                "job":"%s",
                "hobby": "%s"
            }
        "message": "%s"
    }
    """
    resp = resp % (id, name, job, hobby, message)
    return resp, 201, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug = True)
from flask import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def teste():
    print(request.form);
    return Response(f"Recived: ", status=200, mimetype="text/plain")

@app.route('/', methods=['GET'])
def teste2():
    return Response(f"Lorem Ipsum Dolor Sit Amed ", status=200, mimetype="text/plain")

app.run(host="0.0.0.0", port=7777)

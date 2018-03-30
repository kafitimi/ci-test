from flask import Flask, request
from cplx import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return '<h2>Введите вещ и мнимую часть комплексного числа</h2>' \
               '<form method="post">' \
               'x<input id="x" name="x"><br>' \
               'y<input id="y" name="y"><br>' \
               '<input type="submit">'\
               '</form>'
    else:
        return '<h1>Пока не реализовано</h1>'
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
        x = float(request.values.get('x'))
        y = float(request.values.get('y'))
        i = Cplx(x,y)
        return '<h2>Модуль и аргумент комплексного числа x='+str(x)+' y='+str(y)+'</h2>' \
               '<label>Модуль </label>r='+str(i.r())+'<br>'\
               '<label>Аргумент </label>φ='+str(i.arg())+' (рад)'
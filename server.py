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
        z = Cplx(x, y)
        return \
            '<h2>Комплексное число z = '+str(x)+' + '+str(y)+'i</h2>' \
            '<label>Модуль </label>r='+str(z.r())+'<br>'\
            '<label>Аргумент </label>φ='+str(z.arg())+' (рад)'
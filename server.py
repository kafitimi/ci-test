from flask import Flask, request
from cplx import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return '<h2>Введите вещественную и мнимую часть комплексного числа z</h2>' \
               '<form method="post">' \
               'Вещественная часть, x <input id="x" name="x"><br>' \
               'Мнимая часть, y <input id="y" name="y"><br>' \
               '<input type="submit">'\
               '</form>'
    else:
        x = float(request.values.get('x'))
        y = float(request.values.get('y'))
        z = Cplx(x,y)      
        return '<h2>Комплексное число z = ' +str(x)+ ' + ' +str(y)+ 'i</h2>' \
               '<label>Модуль </label>r=' +str(i.r())+ '<br>'\
               '<label>Аргумент φ = ' +str(z.arg())+ ' (рад)</label>'
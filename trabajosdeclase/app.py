from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """"<h1>bienvenido a la calculadora de python </h1>"
"<h2>1.- para sumar escribe en el navegador 127.0.0.1:5000/suma/v1/v2</h2>"
"<h2>2.- para restar escribe en el navegador 127.0.0.1:5000/resta/v1/v2</h1>"
"<h2>3.- para multiplicar escribe en el navegador 127.0.0.1:5000/multiplica/v1/v2</h1>"
"<h2>4.- para dividir escribe en el navegador 127.0.0.1:5000/divide/v1/v2</h1>"
"<h2>5.- para saber el valor maximo y minimo escribe en el navegador 127.0.0.1:5000/maxmin/v1/v2</h1>" """
    
    
@app.route('/devide/<int:v1>/<int:v2>')
def devide(v1,v2):
        if v2!=0:
            resultado =v1/v2
            return f"<h3>{resultado}</h3>"

@app.route('/suma/<int:v1>/<int:v2>')
def suma(v1,v2):
        resultado=v1+v2
        return f"<h3>{resultado}</h3>"

@app.route('/resta/<int:v1>/<int:v2>')
def resta(v1,v2):
        resultado = v1 - v2
        return f"<h3>{resultado}</h3>"
    
@app.route('/multiplica/<int:v1>/<int:v2>')
def multiplica(v1, v2):  
        resultado = v1 * v2
        return f"<h3>{resultado}</h3>"
    
@app.route('/maxmin/<int:v1>/<int:v2>')
def maxmin(v1, v2):
        maximo = max(v1, v2)
        minimo = min(v1, v2)
        return f"<h1>El máximo entre {v1} y {v2} es {maximo}</h1><h1>El mínimo entre {v1} y {v2} es {minimo}</h1>"
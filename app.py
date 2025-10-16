from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/index1')
def animales():
    return render_template('index1.html')

@app.route('/index2')
def vehiculos():
    return render_template('index2.html')

@app.route('/index3')
def maravillas():
    return render_template('index3.html')

@app.route('/acerca')
def acercade():
    return render_template('acerca.html')

@app.route('/secion')
def secion():
    return render_template('secion.html')
 
 
if __name__ == '__main__':
    app.run(debug=True)

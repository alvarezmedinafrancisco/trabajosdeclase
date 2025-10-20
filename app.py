from flask import Flask, render_template, request
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

@app.route('/secion', methods=["GET", "POST"])
def secion():
    error = None
    if request.method == "POST":
        contra = request.form.get("contra")
        newcontra = request.form.get("newcontra")
        boton = request.form.get("boton")
        if not contra or not newcontra:
            error = "este campo es requerido."
        elif contra != newcontra:
            error = "contraseñas no coinciden."
        else:
            error = "contraseña actualizada con exito."
            if boton == "boton":
                return render_template('base.html', error=error)
            
    return render_template('secion.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)

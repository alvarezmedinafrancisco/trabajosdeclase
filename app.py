from flask import Flask, render_template, request , url_for, redirect, session
app = Flask(__name__)

usuario= [{
    "usuario": "admin",
    "contra": "admin123"
}]
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

@app.route('/validalogin', methods=["GET", "POST"])
def validalogin():
    error = None
    if request.method == "POST":
        contra = request.form.get("contra")
        newcontra = request.form.get("newcontra")
        
        
        if not contra or not newcontra:
            error = "Este campo es requerido."
        elif contra != newcontra:
            error = "Las contraseñas no coinciden."
        else:
            error = "Contraseña actualizada con éxito."
            if boton == "boton":
                return render_template('base.html', error=error)
            
    return render_template('registro.html', error=error)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contra = request.form.get("contra")
        
        if not usuario or not contra:
            error = "Este campo es requerido."
        else:
            error = "Registro exitoso."
            return render_template('base.html', error=error)
            
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)

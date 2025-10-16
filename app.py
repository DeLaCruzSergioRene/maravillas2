from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config["SECRET_KEY"] = "una_clave_secreta_muy_larga_y_dificil_de_adivinar"

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/ani")
def animales():
    
    return render_template("animales.html")

@app.route("/veh")
def vehiculos():
    
    return render_template("vehiculos.html")

@app.route("/mar")
def maravillas():
    
    return render_template("maravillas.html")

@app.route("/ace")
def acercas():
    
    return render_template("acerca.html")

@app.route("/ses")
def sesion():
    
    return render_template("sesion.html")

@app.route("/reg")
def registrar():
    
    return render_template("registro.html")

@app.route("/registrame", methods=["GET", "POST"])
def registrame():
    error = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellidos = request.form["apellidos"]
        dia = request.form["dia"]
        mes = request.form["mes"]
        anio = request.form["anio"]
        genero = request.form["genero"]
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        confirmar_contrasena = request.form["confirmar_contrasena"]
        
        
        
if __name__ == "__main__":
    app.run(debug=True)
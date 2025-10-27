from flask import Flask, render_template, request, redirect, url_for, session, flash

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
        
        if len(nombre) < 3:
            flash("El nombre debe tener al menos 3 caracteres.")
            return render_template("registro.html", nombre=nombre)
        
        if len(apellidos) < 3:
            flash("No puede haber menos de 3 caracteres.")
            return render_template("registro.html", apellidos=apellidos) 
        
        if contrasena != confirmar_contrasena:
            error = "La contraseña no coincide."
            
        if error != None:
            flash(error)
            return render_template("registro.html")
        else:
            flash(f"¡Registro exitoso para el usuario: ¡{nombre}!")
            return render_template("index.html")
        
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        confirmar_contrasena = request.form["confirmar_contrasena"]
        
        if len(nombre) < 3:
            flash("El nombre debe tener al menos 3 caracteres.")
            return render_template("sesion.html", nombre=nombre)
        
        if contrasena != confirmar_contrasena:
            error = "La contraseña no coincide."
            
        if error != None:
            flash(error)
            return render_template("sesion.html")
        else:
            session["nombre"] = nombre
            session["email"] = email
            flash(f"¡Registro exitoso para el usuario: ¡{nombre}!")
            return redirect(url_for("index"))
    return render_template("sesion.html")

@app.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()  
    flash("Has cerrado sesión exitosamente.")
    return redirect(url_for("login"))
        
if __name__ == "__main__":
    app.run(debug=True)
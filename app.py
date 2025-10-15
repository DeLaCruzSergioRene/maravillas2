from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
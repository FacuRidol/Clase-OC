from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("index.html")

@app.route("/plantas")
def plantas():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("plantas.html")

@app.route("/milanesa")
def milanesa():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("milanesa.html")

@app.route("/videos")
def videos():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("videos.html")

@app.route("/menu")
def menu():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("menu.html")





if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)
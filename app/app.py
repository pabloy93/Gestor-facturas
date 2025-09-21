from flask import Flask, render_template
import os

# Forzamos la ruta absoluta de la carpeta templates
template_path = os.path.join(os.getcwd(), "templates")
app = Flask(__name__, template_folder=template_path)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

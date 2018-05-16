from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    # return "Hola masdsurtytnadsdsdo"
    return render_template('Probando.html')

if __name__ == "__main__":
    app.run(debug=True)

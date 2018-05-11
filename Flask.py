from flask import flask
app = flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"

if __name__ == "__main__":
    app.run()
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "GSW CAMPEON" , 'asdsad'

if __name__ == "__main__":
    app.run(debug=True)
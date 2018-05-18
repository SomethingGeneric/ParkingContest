from flask import Flask
import parking
from parking import student

#I don't understand flask help

app = Flask(__name__)

f = open("html/index.html")
homepage = f.read()
f.close()

nick= parking.check()
# nick.eval()

@app.route("/")
def index():
    return homepage

@app.route("/check/")
def check():
    return nick.eval()

app.run(host='0.0.0.0',port=2107)

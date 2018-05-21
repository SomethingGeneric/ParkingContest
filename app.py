from flask import Flask
import parking
from parking import student

#I don't understand flask help -kris

app = Flask(__name__)

f = open("html/index.html")
homepage = f.read()
f.close()

nick= parking.check()

# app.route is the url that the user will enter in the browser to get the contents of this function
@app.route("/")
def index():
    app.logger.info('Someone saw the homepage')
    return homepage

# if you were running this locally, you'd enter http://localhost:2107/check to get this
  #string,string,int,string,boolean,boolean,boolean,string
#/<name>/<id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<otherreason>
@app.route("/check/<name>/<Id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<distance>/<otherreason>")
def check(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason):
    stud = student(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason)
    return nick.eval(stud)

# host 0.0.0.0 means run according to the system's policy, port not being on 80 (standard url port) means I won't get rko'd by bot DDOS probably
app.run(host='0.0.0.0',port=2107)

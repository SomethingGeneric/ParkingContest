from flask import Flask
import parking
from parking import student

#I don't understand flask help -kris

app = Flask(__name__)
nick= parking.check()


def serve_raw(name):
    f = open("html/"+name+".html")
    homepage = f.read()
    f.close()
    return str(homepage)



# app.route is the url that the user will enter in the browser to get the contents of this function
@app.route("/")
def index():
    app.logger.info('Someone saw the homepage')
    return serve_raw('index')

@app.route("/kys")
def end():
    quit()

@app.route("/signup")
def welcome():
    app.logger.info('Someone saw the welcome page')
    return serve_raw('signup')

@app.route("/parking.css")
def ouch():
    x = open('html/parking.css')
    f = x.read()
    x.close()
    return f


# if you were running this locally, you'd enter http://localhost:2107/check to get this
  #string,string,int,string,boolean,boolean,boolean,string
#/<name>/<id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<otherreason>
@app.route("/check/<name>/<Id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<distance>/<otherreason>")
def check(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason):
    stud = student(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason)
    
    #nick.eval(stud)

# host 0.0.0.0 means run according to the system's policy, port not being on 80 (standard url port) means I won't get rko'd by bot DDOS probably
app.run(host='0.0.0.0',port=2107)

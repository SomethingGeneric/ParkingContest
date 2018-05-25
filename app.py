from flask import Flask
import parking
import json
from parking import student
from parking import parkingSpace

#I don't understand flask help -kris

app = Flask(__name__)
nick= parking.check()
spacesList = [parkingSpace(False,None)] * 65


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

@app.errorhandler(500)
def error(code):
    return "Kris succ"

@app.errorhandler(404)
def fourofour(code):
    return "Matt and Whit both succ"

# if you were running this locally, you'd enter http://localhost:2107/check to get this
  #string,string,int,string,boolean,boolean,boolean,string
#/<name>/<id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<otherreason>
@app.route("/check/<name>/<Id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<distance>/<otherreason>")
def check(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason):
    stud = student(name,Id,int(grade),bFS(sports),bFS(internship),bFS(dual),bFS(disabilities),float(distance),bFS(otherreason))
    pS = None
    
    for i in spacesList:
        if i.taken == False:
            pS = i
            break
    from_kris = nick.eval(stud, pS)
    print(stud.name + ", " + stud.ID + ", " + stud.grade + ", " + stud.sports + ", " + stud.internship + ", " + stud.dual + ", " + stud.disabilities + ", " + stud.distance+", " + stud.otherreason)
    site = serve_raw("return")
    site = site.replace("$result",from_kris)
    return site
    heff("heff.heck",stud.name + ", " + str(stud.Id) + ", " + str(stud.grade) + ", " + stud.sports + ", " + stud.internship + ", " + stud.dual + ", " + stud.disabilities + ", " + str(stud.distance) + ", " + stud.otherreason)

def bFS(string):
    if string == "true":
        return True
    elif string == "false":
        return False
    else:
        return False
def heff(filename, txtToWrite):
    f = open(filename,'a+')
    f.write(txtToWrite) #or f.write(variable)
    f.close()

# host 0.0.0.0 means run according to the system's policy, port not being on 80 (standard url port) means I won't get rko'd by bot DDOS probably
app.run(host='0.0.0.0',port=2107)

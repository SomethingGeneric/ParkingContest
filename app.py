from flask import Flask
import parking
from parking import student
import email
from email import EmailMsg
import linecache

admin_email = 'webmaster@expeditionventures.co'

#I don't understand flask help -kris

app = Flask(__name__)
nick= parking.check()

#FILE FOR STORAGE
storageFN = 'Students.ls'

e = EmailMsg()

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

@app.route("/space/<number>")
def getSpaceInfo(number):
    return linecache.getline(storageFN, int(number))


# if you were running this locally, you'd enter http://localhost:2107/check to get this
  #string,string,int,string,boolean,boolean,boolean,string
#/<name>/<id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<otherreason>
@app.route("/check/<name>/<Id>/<grade>/<sports>/<internship>/<dual>/<disabilities>/<distance>/<otherreason>")
def check(name,Id,grade,sports,internship,dual,disabilities,distance,otherreason):
    stud = student(name,Id,int(grade),bFS(sports),bFS(internship),bFS(dual),bFS(disabilities),float(distance),bFS(otherreason))
    
    
       
    #CHECKS FOR THE NUMBER OF LINES IN storageFN
    if file_len(storageFN) < 75: 
        from_kris = nick.eval(stud)
        x = "Algorithm result:\n" + from_kris
        e_text = "Name: " + stud.name + ", ID: " + str(stud.ID) + ", Grade: " + str(stud.grade) + ", In sports: " + str(stud.sports) + ", Is an intern: " + str(stud.intern) + ", Is double enrolled: " + str(stud.dual) + ", Any disabilities: " + str(stud.disabilities) + ", Aprox. Distance from school: " + str(stud.distanceInMiles) + ", Contact for other reason: " + str(stud.other_reason)
        f_msg = x + '\n' + e_text
        e.set_msg(admin_email,'Student Signup for '+stud.name,f_msg)
        e.send()
        writeData(stud)
        print("THIS IS THE CURRENT FILE LENGTH: " + str(file_len(storageFN)))
    else:
        from_kris = nick.reject("No vacant spaces")
    site = serve_raw("return")
    site = site.replace("$result",from_kris)
    
    
    return site
    

def bFS(string):
    if string == "true":
        return True
    elif string == "false":
        return False
    else:
        return False
def writeData(Student):
        with open(storageFN, 'a+') as f:
            f.write(Student.name + ", " + str(Student.ID) + ", " + str(Student.grade) + ", " + str(Student.sports) + ", " + str(Student.intern) + ", " + str(Student.dual) + ", " + str(Student.disabilities) + ", " + str(Student.distanceInMiles) + "\n")
            print("yay")

def file_len(fname):
    return len(open(fname).readlines()) 

# host 0.0.0.0 means run according to the system's policy, port not being on 80 (standard url port) means I won't get rko'd by bot DDOS probably
app.run(host='0.0.0.0',port=2107)

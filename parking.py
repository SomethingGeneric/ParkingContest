import re
#Somewhere we need to put a list of a certain number and fill it with preinitialized parking space objects 
#so that we can quickly assign each accepted student to the next available one
class check:
    def __init__(self):
        return
    #Pass in a student object
    def eval(stdnt):
        
        
        if stdnt.grade == 9:
            return reject("Um how drive?")
        elif stdnt.grade == 10:
            return reject("Um how drive?")
        elif stdnt.grade == 11:
            # qualifiers
            if checkID(stdnt) == True:
                if stdnt.distanceInMiles < 1.0:
                    return reject("Um walk?")
                else:
                    if checkForSpecialStuff(stdnt) > 3:
                        return accept(stdnt)
                    
            else:
                reject("ID ain't valid m8")
            
        elif stdnt.grade == 12:
            # conditions
            if checkID(stdnt) == True:
                if stdnt.distanceInMiles < 1.0:
                    return reject("Um walk?")
                else:
                    if checkForSpecialStuff(stdnt) >= 1:
                        return giveParkingSpace(stdnt)
            else:
                reject("ID ain't valid m8")
   #Methods about stuff
    def reject(reason):
        return "Hah no: " + reason
    
    def checkID(Student):
        if len(Student.ID) != 6:
            return False
        elif len(Student.ID == 6):
            #A little unsure if this works
            p = re.compile('[a-zA-Z]')
            if re.match(p, Student.ID):
                return False
            else:
                return True
        

    def checkForSpecialStuff(student):
        #Count how many special things (internship, sports, dual enrollment, disabilities, other reasons)
        count = 0
        if student.sports == True:
            count += 1
        if student.intern == True:
            count += 1
        if student.dual == True:
            count += 1
        if student.disabilities == True:
            count += 1
        if student.other_reason == True:
            count += 1
            
        return count
            
    def giveParkingSpace(student):
        #assign the student to the next available parking space                
            
        
        
#This is the student object that contains all the information required.     

class student:
    #template
    name = ""
    ID = ""
    grade = 9
    sports = False
    intern = False
    dual = False
    disabilities = False
    distanceInMiles = 0.0
    other_reason = ""
    
    #This is the constructor, which defines the variables required to pass in at creation of the object.
    def __init__(self, name, id, grade, sports, intern, dual, disabilities, distance, other_reason):
        self.name = name
        self.ID = id
        self.grade = grade
        self.sports = sports
        self.intern = intern
        self.dual = dual
        self.disabilities = disabilities
        self.distanceInMiles = distance
        self.other_reason = other_reason
    
    
        
        
class parkingSpace:
    taken = False
    number = 0
    student = none
    
    def __init__(self, taken, num, student):
        self.taken = taken
        self.number = num
        self.student = student
      

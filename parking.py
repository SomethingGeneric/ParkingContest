class check:
    def __init__(self):
        return
    #Pass in a student object
    def eval(stdnt):
        if student.grade == 9:
            return reject("Um how drive?")
        elif student.grade == 10:
            return reject("Um how drive?")
        elif student.grade == 11:
            # qualifiers
            checkID(stdnt)
            
        elif student.grade == 12:
            # conditions
            checkID(stdnt)
            
        
        
#This is the student object that contains all the information required.     

class student:
    #template
    name = ""
    email = ""
    grade = 9
    sports = ""
    intern = ""
    dual = False
    disabilities = ""
    other_reason = ""
    
    #This is the constructor, which defines the variables required to pass in at creation of the object.
    def __init__(self, name, email, grade, sports, intern, dual, disabilities, other_reason):
        self.name = name
        self.email = email
        self.grade = grade
        self.sports = sports
        self.intern = intern
        self.dual = dual
        self.disabilities = disabilities
        self.other_reason = other_reason
    
    def reject(reason):
        return "Hah no: " + reason
    
    def checkID(Student):
        #Search database for ID
        #If its in the database return yes
        #if its not in the database return nah
        
    
    
      

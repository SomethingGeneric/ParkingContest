class check:
    def __init__(self):
        return
    #Pass in a student object
    def eval(student):
        if student.grade == 9:
            return "No pass for you. How can you even drive??"
        elif student.grade == 10:
            return "Logged the special reason below, you'll hear from administrators soon, hopefully."
        elif student.grade == 11:
            # qualifiers
            return
        elif student.grade == 12:
            # conditions
            return
        
class student:
    name = ""
    email = ""
    grade = 9
    sports = ""
    intern = ""
    dual = false
    disabilities = ""
    other_reason = ""
    
    def __init__(self, name, email, grade, sports, intern, dual, disabilities, other_reason):
        self.name = name
        self.email = email
        self.grade = grade
        self.sports = sports
        self.intern = intern
        self.dual = dual
        self.disabilities = disabilities
        self.other_reason = other_reason
    
      

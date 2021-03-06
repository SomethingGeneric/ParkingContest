import re
#Somewhere we need to put a list of a certain number and fill it with preinitialized parking space objects
#so that we can quickly assign each accepted student to the next available one
class check:
    def __init__(self):
        return
    #Pass in a student object
    def eval(self,stdnt):


        if stdnt.grade == 9:
            return self.reject(self.checkForSpecialStuff(stdnt))
        elif stdnt.grade == 10:
            return self.reject(self.checkForSpecialStuff(stdnt))
        elif stdnt.grade == 11:
            # qualifiers
            if self.checkID(stdnt) == True:
                if stdnt.distanceInMiles < 1.0:
                    return self.reject(self.checkForSpecialStuff(stdnt))
                else:
                    if self.checkForSpecialStuff(stdnt) > 3:
                        return self.accept(self.checkForSpecialStuff(stdnt))
                    else:
                        return self.reject(self.checkForSpecialStuff(stdnt))

            else:
                return self.reject(self.checkForSpecialStuff(stdnt))

        elif stdnt.grade == 12:
            # conditions
            if self.checkID(stdnt) == True:
                if stdnt.distanceInMiles <= 1.0:
                    return self.reject(self.checkForSpecialStuff(stdnt))
                else:
                    if self.checkForSpecialStuff(stdnt) >= 1:
                        return self.accept(self.checkForSpecialStuff(stdnt))
                    else:
                        return self.reject(self.checkForSpecialStuff(stdnt))
            else:
                return self.reject(self.checkForSpecialStuff(stdnt))
        else:
            return self.reject(self.checkForSpecialStuff(stdnt))
   #Methods about stuff
    def reject(self,score):
        return "Hah Here's your score lol: " + str(score) + ". Sent to the administrator."
    def accept(self, score):
        return "Hah Here's your score lol: " + str(score) + ". Sent to the administrator and saved."

    def checkID(self,Student):
        if len(Student.ID) != 6:
            return False
        elif len(Student.ID) == 6:
            #A little unsure if this works
            p = re.compile('[a-zA-Z]')
            if re.match(p, Student.ID):
                return False
            else:
                return True


    def checkForSpecialStuff(self,student):
        #Count how many special things (internship, sports, dual enrollment, disabilities, other reasons)
        count = 0
        if student.sports == True:
            count += 1
        if student.intern == True:
            count += 2
        if student.dual == True:
            count += 1.5
        if student.disabilities == True:
            count += 2
        if student.other_reason == True:
            count += 0.5

        return count



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
    other_reason = False

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
    student = None
    number = 0

    def __init__(self, taken, student):
        self.taken = taken
        self.student = student
        self.number = 0


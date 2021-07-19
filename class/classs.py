####################################################################
#CLASS: Building, University, Human, Student, Lecturer
#FUNCTION: __init__, work_and_study, print_humans, __repr__
#BRIEF: 
#PARAMS: different classes different parameters
#OUTPUT: different output
#RETURN: different return
####################################################################


#CLASS: Building
class Building():
    #receives arguments(self,walls,stairs,windows,roof)
    def __init__(self,walls,stairs,windows,roof):
        self.walls = walls
        self.stairs = stairs
        self.windows = windows
        self.roof = roof


#CLASS: University inherits from class Building
class University(Building):
    #receives arguments(self,walls,stairs,windows,roof,name,adress)
    def __init__(self,walls,stairs,windows,roof,name,adress):
        super().__init__(walls,stairs,windows,roof)
        self.name = name
        self.adress = adress
        self.StLe = []
    
    #receives arguments(self,*human),*human-these are objects class Student and Lecturer
    def work_and_study(self,*human):
        for h in human:
            self.StLe.append(h)
    
    #screens who studies and works at this university
    def print_humans(self):
        for s in self.StLe:
            print("we study and work -"+str(s))

    #returns name University and address
    def __repr__(self):
        return self.name+ " "+self.adress


#CLASS: Human
class Human():
    #receives arguments(self,name,surname,age)
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age


#CLASS: Student inherits from class Human
class Student(Human):
    #receives arguments(self,name,surname,age,specialty)
    def __init__(self,name,surname,age,specialty):
        super().__init__(name,surname,age)
        self.specialty = specialty
    
    #returns Student---name,surname,age,specialty
    def __repr__(self):
        return self.name+" "+self.surname+" "+str(self.age)+" "+self.specialty


#CLASS: Lecturer inherits from class Human
class Lecturer(Human):
    #receives arguments(self,name,surname,age,profession)
    def __init__(self,name,surname,age,profession):
        super().__init__(name,surname,age)
        self.profession = profession
    
    #returns Lecturer---name,surname,age,profession
    def __repr__(self):
        return self.name+" "+self.surname+" "+str(self.age)+" "+self.profession


#create objects
pers1 = Student("John","Johnson",25,"Physicist")
print(pers1)
pers2 = Lecturer("Samuel","Adamson",34,"Programmer")
print(pers2)
GPMH = University(4,200,300,1,"Gyumru Petakan Mankavarjakan Hamalsaran","Paruyr Sevak 4")
print(GPMH)
GPMH.work_and_study(pers1,pers2)
GPMH.print_humans()

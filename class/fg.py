####################################################################
#CLASS: human,employer,manager
#FUNCTION: fire,hier
#BRIEF:
#PARAMS: (self,name,age,profesia)
#OUTPUT:
#RETURN: 
####################################################################
class human():
    #receives arguments(self,name,age)
    def __init__(self, name, age):
        self.name = name
        self.age = age

class employer(human):
    #receives arguments(self,name,age,profesia),inherits arguments from human class(name,age)
    def __init__(self,name,age,profesia):
        super().__init__(name,age)
        self.profesia = profesia

class manager(employer):
    #receives arguments(self,name,age,profesia,fire,hier),inherits arguments from employer class(name,age,profesia)
    def __init__(self,name,age,profesia,fire=[],hier=[],staf=[]):
        super().__init__(name,age,profesia)
        self.fire = fire
        self.hier = hier
        self.staf = staf

#receives arguments (name,target)
def fire(name,target):
    for i in range(len(name)):
        if name[i] == target:
            fires.append(name[i])
            print("hercvac e")
        else:
            print("nman mard chka")

#receives arguments (name,target)
def hier(name,target):
    s=-1
    for i in range(len(name)):
        s+=1
        if name[i] == target:
            hiers.append(name[i])
            print("vercnum enq ashxatanqi")
            stafs.pop(s)
        else:
            print("nman ashxatox ka")

#call main
def main():
    pers1 = employer("John",20,"programist")
    pers2 = employer("Tom",34,"doctor")
    pers3 = employer("Jack",43,"teacher")
    manager1 = manager("Bob",45,"Professor")
    fires = manager1.fire
    hiers = manager1.hier
    stafs = manager1.staf
    stafs.append(pers1)
    stafs.append(pers2)
    hiers.append(pers3)
    f = fire(manager1.staf,"David")
    h = hier(manager1.staf,"Bob")

#check main
if __name__ == "__main__":
    main()

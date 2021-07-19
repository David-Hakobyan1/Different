class Human():
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age
    
    def set_name(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name,self.__surname,self.__age

#person1 = Human("John","Johnson",39)
#print(person1.get_name())
#person1.set_name("John","Johnson",32)
#print(person1.get_name())

class mard():
    def __init__(self,name,surname,age):
        print("init")
        self.__name = name
        self.__surname = surname
        self.__age = age

    def p(self):
        print(self.__age)

    @property
    def age(self):
        print("getting")
        return self.__age

    @age.setter
    def age(self,age):
        print("setting")
        self.__age = age
        if age > 0:
            self.__age = age
        else:
            self.__age = "mutq 0 ic mec tiv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
        if name == "Armen":
            self.__name = name
        else:
            self.__name = "gzl"
    def __int__(self):
        return 5

person2 = mard("aper", "jan", -1)
person2.age = -1
person2.name = "vle"
print(person2[4])
print(person2.age, person2.name, int(person2))

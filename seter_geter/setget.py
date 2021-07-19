####################################################################
#CLASS: mard
#FUNCTION: __init__, set_name, set_age, set_surname
#BRIEF:
#PARAMS: (self,name,surname,age)
#OUTPUT:
#RETURN: self.__name, self.__surname, self.__age
####################################################################

class mard:
    #receives arguments(self,name,surname,age)
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age
    
    #checking if parameters are correct name
    def set_name(self,name):
        if name.isalpha():
            self.__name = name
        else:
            self.__name = "sxal anuni mutq"
    
    #checking if parameters are correct age
    def set_age(self,age):
        if age >= 0:
            self.__age = age
        else:
            self.__age = "sxal tariqi mutq"
    
    #checking if parameters are correct surname
    def set_surname(self,surname):
        if surname.isalpha():
            self.__surname = surname
        else:
            self.__surname = "sxal azganuni mutq"
    
    #return self.__name,self.__surname,self.__age
    def get_a(self):
        return self.__name,self.__surname,self.__age

#create a character and give parameters,display the result on the screen
person = mard("Valod","Petrosyan",45)
print(person.get_a())
person.set_name("Gabriel")
person.set_age(5)
person.set_surname("Poxosyan")
print(person.get_a())

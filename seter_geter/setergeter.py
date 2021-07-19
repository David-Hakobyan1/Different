####################################################################
#CLASS: human
#FUNCTION: __init__, @property-@name.setter, @property-@surname.setter, @property-@age.setter
#BRIEF:
#PARAMS: (self,name,surname,age)
#OUTPUT:
#RETURN: self.__name, self.__surname, self.__age
####################################################################
class human:
    #receives arguments(self,name,surname,age)
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age
    
    #return self.__name
    @property
    def name(self):
        return self.__name
    
    #checking if parameters are correct name
    @name.setter
    def name(self,name):
        if name.isalpha():
            self.__name = name
        else:
            self.__name = "sxal anvan mutq"
    
    #return self.__surname
    @property
    def surname(self):
        return self.__surname
    
    #checking if parameters are correct surname
    @surname.setter
    def surname(self,surname):
        if surname.isalpha():
            self.__surname = surname
        else:
            self.__surname = "sxal azganvan mutq"
    
    #return self.__age
    @property
    def age(self):
        return self.__age
    
    #checking if parameters are correct age
    @age.setter
    def age(self,age):
        if age >= 1:
            self.__age = age
        else:
            self.__age = "sxal tariqi mutq"

#create a character and give parameters,display the result on the screen
pers1 = human("Armen","Hakobyan",46)
pers1.name = "Artur"
pers1.age = 18
pers1.surname = "Davtyan"
print("Anun - "+pers1.name+",Azganun - "+pers1.surname+",Tariq - "+str(pers1.age))

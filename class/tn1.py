####################################################################
#CLASS: number
#FUNCTION: __init__,__eq__,__ne__,__lt__,__gt__,__le__,__ge__
#BRIEF: Magic comparison methods
#PARAMS: (number)
#OUTPUT:
#RETURN: self.number,other.number
####################################################################
class number:
    def __init__(self,number):
        self.number = number
    
    #Defines the behavior of the equality operator( == , __eq__)
    def __eq__(self,other):
        return self.number == other.number
    
    #Defines the behavior of the inequality operator( != , __ne__)
    def __ne__(self,other):
        return self.number != other.number
    
    #Defines the behavior of the less than operator( < , __lt__)
    def __lt__(self,other):
        return self.number < other.number

    #Defines the behavior of the more operator( > , __gt__)
    def __gt__(self,other):
        return self.number > other.number

    #Specifies the behavior of the less than or equal operator( <= , __le__)
    def __le__(self,other):
        return self.number <= other.number

    #Specifies the behavior of the greater than or equal operator( >= , __ge__)
    def __ge__(self,other):
        return self.number >= other.number

#check example
d1 = number(2)
d2 = number(3)
print(d1 != d2) #return True
print(d1 == d2) #return False

#compare b1 and b2, and display
def compare(b1,b2):
    if b1 == b2:
        print("havasar en")
    #elif b1 != b2:
        #print("havasar chen")
    elif b1 > b2:
        print("arajin@ mec e erkrordic")
    elif b1 < b2:
        print("arajin@ poqr e erkrordic")
   #elif b1 >= b2:
       #print("arajin@ mece kam havasar e erkrordin")
   #elif b1 <= b2:
       #print("arajin@ poqre kam havasar e erkrordin")

#call function
def main():
    b1 = number(1)
    b2 = number(2)
    compares = compare(b1,b2)

#check main
if __name__ == "__main__":
    main()

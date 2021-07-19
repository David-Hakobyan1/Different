class vo:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __eq__(self,other):
        return self.a == other.a
    
    #def __ne__(self,other):
        #return self.a != other.a

c=vo(7,"jan")
z=vo(8,"gto")
print(c==z)


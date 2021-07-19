class box:
    def __init__(self,w,h,l):
        self.width = w
        self.hight = h
        self.lenght = l
    def __add__(self,other):
        return box(self.width + other.width ,self.hight,self.lenght)
    def __str__(self):
        return "{},{},{}".format(self.width,self.hight,self.lenght)
    
b1 = box(10,5,7)
b2 = box(8,12,20)
print(b1+b2)

class house(box):
    def __init__(self,w,h,l,wi,de):
        super().__init__(w,h,l)
        self.wi = wi
        self.de = de 
    def __str__(self):
        mstr=super().__str__()
        return mstr+","+str(self.wi)+" "+str(self.de)
h1 = house(10,5,7,16,2)
print(h1)

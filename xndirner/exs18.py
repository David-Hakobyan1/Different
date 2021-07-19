class Human:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return str((self.name,self.age,self.surname))

human1 = Human('Vahan','Papikyan',20)
human2 = Human('David','Hakobyan',30)
human3 = Human('Arman','Poghosyan',26)
human4 = Human('Vardan','Petrosyan',46)
human5 = Human('Poghos','Papikyan',20)

l=[]
l.append(human1)
l.append(human2)
l.append(human3)
l.append(human4)
l.append(human5)

print(sorted(l,key=lambda x:x.name.lower()))
print(sorted(l,key=lambda x:x.age))
print(sorted(l,key=lambda x:x.surname.lower()))

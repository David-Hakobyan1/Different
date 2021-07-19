class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{},{} ".format(self.name,self.age)

class employer(human):
    pass


class manager(human):
    pass

class directors(manager):
    pass

mard = directors("ds",45)
print(mard)

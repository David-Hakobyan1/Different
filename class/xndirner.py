class mard:
    def __init__(self):
        self.__name=""
        self.__age=0
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self,f):
        if len(f.split)<2:
            self.name = ""
        else:
            self.name = f

hm = mard()
hm["name = "val"

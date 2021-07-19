from jinja2 import Template

# Orinak 1_______________________________________________________________
#nam = "artak"
#tariq = 30
#temp = Template("barev dzez {{name.upper()}} yes {{year*2}} tarekan em")
#msg = temp.render(name = nam,year = tariq)
#print(msg)
#________________________________________________________________________

# Orinak 2 class_________________________________________________________
#class Person:
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age

#per = Person("David",30)
#temp = Template("barev dzez {{p.name}} yes {{p.age}} tarekan em")
#msg = temp.render(p = per)
#print(msg)
#________________________________________________________________________

# Orinak 3 class_________________________________________________________
#class Person:
 #   def __init__(self,name,age):
 #       self.name = name
  #      self.age = age

#    def getName(self):
 #       return self.name
    
  #  def getAge(self):
   #     return self.age

#per = Person("David",30)
#temp = Template("barev dzez {{p.getName()}} yes {{p.getAge()}} tarekan em")
#msg = temp.render(p = per)
#print(msg)
#________________________________________________________________________

# Orinak 4 dict__________________________________________________________
#per = {"name":"David","age":28}
#temp = Template("barev dzez {{p.name}} yes {{p.age}} tarekan em")
#msg = temp.render(p = per)
#print(msg)
#________________________________________________________________________

# Orinak 5 dict__________________________________________________________
#per = {"name":"David","age":28}
#temp = Template("barev dzez {{p['name']}} yes {{p['age']}} tarekan em")
#msg = temp.render(p = per)
#print(msg)
#________________________________________________________________________

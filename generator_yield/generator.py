#st = "Hello My WoRld"
#def generator_function(st):
 #   for i in st:
  #      if i.islower():
   #         yield i.upper()
#i=generator_function(st)
#next(i)
#for j in i:
 #   print(j)

st = "hello my world"
def generator(st):
    s=""
    for i in st:
        if i != " ":
            s+=i
            if len(s)>4:
                yield s
                s=""
a = generator(st)
for j in a:
    print(j)

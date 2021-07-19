my_dict={1:"red",2:"green",3:"black",4:"white",5:"black"}
ml=[list(el) for el in my_dict.items()]
#print(ml)
d="121"
s=d[::-1]
print(s)
bol=True
while True:
    c=int(d)+int(s)
    c=str(c)
    if c == c[::-1]:
        print(c)
        break
    s=d

    

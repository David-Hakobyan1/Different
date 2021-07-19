# Milionater )))

import random

gamer = raw_input("user name: ")

def skizb():
   d = {0:{"harc":"hayoc arqa Tigran...","patasxan":("arcat?","erkat?","hzor?","mec?"),"chisht":"mec","bol":False},\
        1:{"harc":"hay @mbish Artur...","patasxan":("Araqelyan?","Aleqsanyan?","Petrosyan?","Kirakosyan?"),"chisht":"Aleqsanyan","bol":False},\
        2:{"harc":"kacin?...","patasxan":("axper?","exbayr?","urag?","mec?"),"chisht":"axper","bol":False},\
        3:{"harc":"dzaxord?...","patasxan":("axper?","panos?","gazan?","mec?"),"chisht":"panos","bol":False}}
    return d
my_dict = skizb()
my_dict=skizb()
d = {}
l=[]
def xax(my_dict):
    dc=0
    c=0
    for i in range(0,len(my_dict)):
        if my_dict[i]["bol"] == False:
            dc+=1
    if dc != 2:
        s = random.randrange(0,len(my_dict))
        if my_dict[s]["bol"] != False:
            xax(my_dict)
        print(my_dict[s]["harc"])
        for i in my_dict[s]["patasxan"]:
            print(i)
        n = raw_input("dzer patasxann e? ")
        if n == my_dict[s]["chisht"]:
            print("chisht e")
            c+=1
            l.append(c)
        else:
            print("sxale")
        my_dict[s]["bol"]=True
        xax(my_dict)
    if dc == 2:
        c=0
        for i in l:
            c+=i
        d[gamer]=c
        f = open("file6.txt","a")
        f.write(str(d))
        f.close()
        return "avart"
xax(my_dict)

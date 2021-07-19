import random

gamer = raw_input("mutq dzer anun@: ")
lis1 = ["aleqsanyan","mec"]

def open_file():
    with open("file2.txt") as f:
        return f.read()

def filter_file(lis):
    st=""
    l=[]
    for i in lis:
        if i.isalpha() or i == " " or i == "?" or i == "@":
            st+=i
        if i=="," or i == "\n":
            l.append(st)
            st=""
    return l[0]

def miavor(lis,lis1,dm):
    c=0
    d={}
    t=0
    while True:
        t+=1
        print(dm)
        if t<5:
            n = raw_input("Mutq: ")
            if n in lis and n in lis1:
                c+=1
                print("chisht e")
                lis1.remove(n)
            else:
                print("sxal e")
        else:
            d[gamer]=c
            return d

def main():
    ml = open_file()
    dm = filter_file(ml)
    cm = miavor(ml,lis1,dm)
    print(cm)
main()

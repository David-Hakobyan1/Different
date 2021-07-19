# Bararan )))

def open_file():
    with open("x1.txt") as f:
        return f.read()

def filter_file(fc):
    st = ""
    l=[]
    for i in fc:
        if i != "\n":
            st+=i
        else:
            s=st.split("-")
            l.append(s)
            st=""
    return l

def bararan(l):
    lis=[]
    lis1=[]
    n = raw_input("mutq bar: ")
    for j in range(len(l)):
        if n == l[j][0]:
            print(l[j][1])
            ab = raw_input("avelacreq bari bacatrutyun: ")
            lis.append(l[j][0])
            lis.append(l[j][1]+","+ab)
            lis1.append(lis)
        else:
            lis1.append(l[j])
    return lis1

def filter_lis(lis1):
    st=""
    c=0
    for i in lis1:
        for j in i:
            st+=j
            c+=1
            if c==1:
                st+="-"
            else:
                st+="\n"
                c=0
    return st

def return_file(st):
    with open("x1.txt","w") as f:
        f.write(st)

def main():
    f=open_file()
    filtered_file=filter_file(f)
    my_bararan=bararan(filtered_file)
    filter_list=filter_lis(my_bararan)
    print(filter_list)
    verj=return_file(filter_list)
main()

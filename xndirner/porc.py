bar = raw_input("mutq bar ")
b = raw_input("mutq tarer ")

# COUNT 1,2 )))
def my_count(x,y):
    counter = len(x.split(y))-1
    print("count -",counter)
#my_count(bar,b)

def my_count2(x,y):
    e = 0
    c = 0
    for i in range(len(x)):
        if x[i] != y[e]:
            e = 0
        if x[i] == y[e]:
            e += 1
            if e == len(y):
                c += 1
                e = 0
                continue
    print("count -",c)
#my_count2(bar,b)
# END COUNT )))

# FIND   )))
def my_find(x,y):
    e = 0
    c = 0
    for i in range(len(x)):
        c += 1
        if x[i] != y[e]:
            e = 0
        if x[i] == y[e]:
            e += 1
            if e == len(y):
                print("find -",c-len(y))
                break
    if y not in x:
            print(-1)
my_find(bar,b)
# END FIND  )))
                
# STRIP )))        
def my_strip(x,y):
    start = 0
    end = 0
    count = 0
    for i in x:
        if i not in y:
            start = count
            break
        count +=1
    count = 0
    for i in range(-1, 0-len(x), -1):
        if x[i] not in y:
            end = count
            break
        count +=1
    end =  0 - end
    print x[start: end]
#my_strip(bar,b)
# END STRIP )))

# SPLIT )))
def my_split(x,y):
    st = ""
    lis = []
    e = 0
    for i in range(len(bar)):
        if x[i] != y[e]:
            st += x[i]
            e = 0
        if x[i] == y[e]:
            e += 1
            if e == len(y):
                lis.append(st)
                e = 0
                st = ""
    lis.append(st) 
    print(lis)
#my_split(bar,b)
# END SPLIT )))

# UPPER )))
#bar = raw_input("mutq bar ")
def my_upper(x):
    st = ""
    st1 = ""
    for i in x:
        if ord(i) > 96 and ord(i) < 123: 
            st = ord(i) - 32
            st1 += chr(st)
        else:
            st = i
            st1 += st
    print(st1)
#my_upper(bar)
# END UPPER )))

# LOWER )))
#bar = raw_input("mutq bar: ")
def my_lower(x):
    st = ""
    st1 = ""
    for i in x:
        if ord(i) > 64 and ord(i) < 91:
            st = ord(i) + 32
            st1 += chr(st)
        else:
            st = i
            st1 += st
    print(st1)
#my_lower(bar)

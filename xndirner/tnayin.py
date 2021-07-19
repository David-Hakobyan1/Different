# Home work 1 )))
ml1 = [{"name":"James","id":1},
       {'name': 'John','id':2}]#,
      # {'name': 'David','id':5},
      # {'name': 'Michael','id':7},
      # {'name': 'William','id':15}]

ml2 = [{'name':'James','id':1},
       {'name': 'John','id':2},
       {'name': 'Paul','id':3}]#,
      # {'name': 'Robert','id':8}]

lis = []
lis1 = []
num1 = -1
num2 = -1

for i in ml1:
    a = i["id"]
    lis.append(a)
for j in ml2:
    b = j["id"]
    lis1.append(b)

def name_id(x,y):
    global num1
    for i in x:
        num1 += 1
        if i not in y:
            print(ml2[num1])
            print(ml2[num1]["name"])
            print(ml2[num1]["id"])# or print (i)
    global num2
    for j in y:
        num2 += 1
        if j not in x:
            print(ml1[num2])
            print(ml1[num2]["name"])
            print(j)# or print(ml1[num2]["id"])
name_id(lis1,lis)

#Home work 2, Richest Customer Wealth example1, Version1 )))
a = 0
st = 0
st1 = 0
accounts = [[1,2,3],[3,2,1]]
for i in range(0,len(accounts)):
    for j in accounts[0]:
        st += j
        a += 1
        if a == 3:
            nor = st
            #print("1st customer has wealth = 1 + 2 + 3 = " + str(st))
        if a > 3:
                st1 += j
#print("2nd customer has wealth = 3 + 2 + 1 = " + str(st1))
if nor == st1:
    print(nor)

# example1, Version2 )))
z = 0
z1 = 0
for i in range(0,len(accounts)-1):
    for h in accounts[i]:
        z += h
for j in range(1,len(accounts)):
    for h in accounts[j]:
        z1 += h
def stugum(x,y):
    if x == y:
        return x # or print(x)
print(stugum(z,z1))# or stugum(z,z1)
 
# Home work3,Richest Customer Wealth example2 )))
z = 0
z1 = 0
z2 = 0
accounts = [[1,5],[7,3],[3,5]]
for i in range(len(accounts)-2):
    for h in accounts[i]:
        z += h
        print("h is 1 - ",h)
for j in range(1,len(accounts)-1):
    for h in accounts[j]:
        print("h is 2 - ",h)
        z1 += h
for g in range(2,len(accounts)):
    for h in accounts[g]:
        print("h is 3 - ",h)
        z2 += h
def stugum_example2(x,y,z):
    if y<x>z:
        return x
    elif x<y>z:
        return y
    else:
        return z
print(stugum_example2(z,z1,z2))

#Home work4,Richest Customer Wealth example3 )))
z = 0
z1 = 0
z2 = 0
accounts = [[2,8,7],[7,1,3],[1,9,5]]
for i in range(len(accounts)-2):
    for h in accounts[i]:
        z += h
        print("h is 1 - ",h)
for j in range(1,len(accounts)-1):
    for h in accounts[j]:
        print("h is 2 - ",h)
        z1 += h
for g in range(2,len(accounts)):
    for h in accounts[g]:
        print("h is 3 - ",h)
        z2 += h
def stugum_example3(x,y,z):
    if y<x>z:
        return x
    elif x<y>z:
        return y
    else:
        return z
print(stugum_example3(z,z1,z2))

#Home work5,Number of Good Pairs example1 )))
nums = [1,2,3,1,1,3]
c = 0
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if nums[i] == nums[j] and i < j:
            c+=1
print(c)

#Home work6,Number of Good Pairs example2 )))
c = 0
nums = [1,1,1,1]
for i in range(0,len(nums)):
    for j in range(1,len(nums)):
        if nums[i] == nums[j] and i < j:
            c += 1
print(c)

#Home work7,Number of Good Pairs example3 )))
c = 0
for i in range(0,len(nums)):
    for j in range(1,len(nums)):
        if nums[i] == nums[j] and i < j:
            c += 1
        else:
            c = 0
print(c)

#Home work8,Jewels and Stones example1 )))
jewels = "aA"
stones = "aAAbbbb"
for i in range(len(jewels)):
    for j in jewels[i]:
        for h in stones:
            if j == h:
                c += 1
print(c)

#Home work9,Jewels and Stones example2 )))
jewels = "z"
stones = "ZZ"
for i in range(len(jewels)):
    for j in jewels[i]:
        for h in stones:
            if j == h:
                c += 1
            else:
                c = 0
print(c)
# END HOME WORKS )))

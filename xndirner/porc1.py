# MINIMUM, MAXIMUM
# orinak 1
#lis1 = [231,24,123,45,611]
#lis1.sort()
#print(lis1[0],lis1[-1])   

# orinak 2
#lis = [231,24,123,45,611]
#a = lis[0]
#b = lis[0]
#for i in lis:
#    if i < a:
 #       a = i
  #  elif i > b:
   #     b = i
#print("minimum = ",a,"maximum = ",b)

lis = [-67,-122,-53,-65,-11,-58,-68]
l = []
arajinmec = lis[0]
yerkrordmec = lis[1]
for i in lis:
    if i > arajinmec:
        yerkrordmec = arajinmec
        arajinmec = i
    elif i > yerkrordmec:
        yerkrordmec = i
print (yerkrordmec)

arajinpoqr = lis[0]
yerkrordpoqr = lis[1]
for j in lis:
    if j < arajinpoqr:
        yerkrordpoqr = arajinpoqr
        arajinpoqr = j
    elif j < yerkrordpoqr:
        yerkrordpoqr = j
print(yerkrordpoqr)

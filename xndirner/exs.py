#1 ############################## list
mlist = [12,34,26,31,108,210]
max=0
for i in mlist:
    i>max
    max=i
#print(max)
######################

#2 ##############################
nlist = ['asb','dfds','vfsv','a','324']
count=0
for i in nlist:
    for j in nlist:
        if i!=j and i[0]==j[0] and len(i)>2:
            count+=1
#print(count)

#3 ################################
slist =['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
n=5
st = ''
alist=[]
count=-1
for j in slist:
    nlist=[]
    count+=1
    for i in range(count,len(slist),5):
        nlist.append(slist[i])
    alist.append(nlist)
    if count==3:
        break
print(alist)

#4 #######################
color1=["red", "orange", "green", "blue", "white"]
color2=["black", "yellow", "green", "blue"]
color_dif=[]
for i in color1:
    if i not in color2:
        color_dif.append(i)
print(color_dif)

#5 #########################
 

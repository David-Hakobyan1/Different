# 1 exercises ####################################################
sample_data = {"math":81,"pysics":83,"chemistry":87}
expected_data = [("chemistry",87),("physick",83),("math",81)]
data=sorted(sample_data.items(),key=lambda x:x[1],reverse=True)
#print(data)
################################################################

# 2 exercises #####################################################
original_dict = {'c1':'Red','c2':'green', 'c3':None}
new_dict={}
for key, value in original_dict.items():
    if value!=None:
        new_dict[key]=value
#print(new_dict)
###############################################################

# 3 exercises ###################################################################
my_dict={'Cierra':175,'Alden Cantrell':180, 'Kierra Gentry':165, 'Pierre':190}
my_ndict={}
#number=input('enter the number: ')
#for key, value in my_dict.items():
 #   if value>number:
  #      my_ndict[key]=value
#print(my_ndict)
##############################################################################

# 4 exercises #############################################################
orig_list=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
ndict={}
for i in orig_list:
    lst=[]
    if i[0] in ndict:
        lst.append(ndict[i[0]])
        lst.append(i[1])
        ndict[i[0]]=lst
    else:
        ndict[i[0]]=i[1]
#print(ndict)
#######################################################################

# 5 exercises ##########################################################
Or_list=[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
nlist=[]
clist=[]
for x in range(len(Or_list)):
    for j in Or_list:
        if Or_list[x]==j and j not in nlist:
            nlist.append(j)

for i in nlist:
    count=0
    for k in Or_list:
        if i==k:
            count+=1
    clist.append(count)
my_tup=(nlist,clist)
#print(my_tup)
#####################################################################

# 6 exercises #######################################################
lst=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
lst.sort()
print(lst)
#####################################################################

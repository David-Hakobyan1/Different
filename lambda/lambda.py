
baz = lambda x,y,z=2:x*y*z
print(baz(2,3))

a = (2,3,4,5,6,3,9,7,8)
lis = list(filter(lambda x: x % 2 != 0,a))
print(lis)

ls = [1,2,3,4,5,6]
l = list(map(lambda x:x*2,ls))
print(l)

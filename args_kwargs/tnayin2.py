def kw(**kwargs):
    return kwargs
d = kw(a = 10,b = 20,c = 30)
#print(d)
def arg(*args):
    e = 0
    for i in args:
        e += i
    return e
lis = [2,6,7]
#print(arg(*lis))
def defa(name = "France"):
    return "I from " + str(name)
#print(defa("London"))


bar = "hello"
md = {}
for el in bar:
    if el in md:
        md[el]+=1
    else:
        md[el]=1
#print(md)
bar = "hello world"
b = "l"
def ft(mstr,delim):
    start = 0
    stop = 0
    count = 0
    for i in range(len(mstr)):
        if mstr[i] == delim:
            start = i
            break
    for i in range(len(mstr)-1,-1,-1):
        if mstr[i] == delim:
            stop = i
            break
    return mstr[start+1:stop]
print(ft(bar,b))


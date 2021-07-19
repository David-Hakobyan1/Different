# Lstrip )))
bar = raw_input("mutq: ")
def my_lstrip(bar):
    start = 0
    for i in range(len(bar)):
        if bar[i] != " ":
            break
        start = i+1
    return bar[start:len(bar)]
#print(my_lstrip(bar))

# Rstrip )))
def my_rstrip(bar):
    stop = -1
    for i in range(-1,0-len(bar),-1):
        if bar[i] != " ":
            break
        stop = i
    return bar[:stop]
#print(my_rstrip(bar))

# Swapcase )))
def my_swapcase(bar):
    st = ""
    for i in  bar:
        if 64<ord(i)<91:
            st += chr(ord(i) + 32)
        elif 96<ord(i)<123:
            st += chr(ord(i) - 32)
        else:
            st += i
    return st
#print(my_swapcase(bar))

# Isspase )))
def my_isspace(bar):
    bol = True
    for i in bar:
        if ord(i)>32:
            bol = False
            break
    return bol
print(my_isspace(bar))

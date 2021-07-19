# Rstrip )))
bar = raw_input("mutq: ")
def my_rstrip(bar):
    count = 0
    start = 0
    for i in range(-1,0-len(bar),-1):
        if bar[i] == " ":
            count += 1
        elif bar[i] != " ":
            stop = count
            break
    stop = 0 - stop
    return bar[0:stop]
print(my_rstrip(bar))



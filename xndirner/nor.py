#n = int(input("mutq: "))
def my_fibonachi(n):
    a = 0
    b = 1
    if n < 0:
        return "mutqagreq 1-ic mec tiv"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
            print(b)
        return b
#my_fibonachi(n)

#replace
bar = "bari ereko"
b = "ri"
c = "9999"
e = 0
s = ""
st = ""

for i in range(len(bar)):
    if bar[i] == b[e]:
        s += bar[i]
        e += 1
        if e == len(b):
            st += c
            e = 0
    else:
        st+=bar[i]
print(st)


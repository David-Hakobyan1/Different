st = "Hello my world"
def func(st):
    for i in st:
        yield ord(i)

d = func(st)
print(next(d))
print(next(d))


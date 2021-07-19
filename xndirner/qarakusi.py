from turtle import *
a = int(input("mutq tiv :"))
def rec(x):
    if x<1:
        return
    else:
        forward(x)
        right(90)
        rec(0.9*x)
        return

rec(a)

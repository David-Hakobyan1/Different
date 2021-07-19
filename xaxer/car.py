from turtle import *
a = int(input("mutq tiv :"))
def tree(x):
    if x<1:
        return
    else:
        forward(x)
        left(45)
        tree(x/2)
        right(90)
        tree(x/2)
        left(45)
        back(x)
    return

left(90)
tree(a)
hideturtle()

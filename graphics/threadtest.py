import threading
import time
from graphics import *

win = GraphWin("porcs",600,600)
G_V = 7
color = "white"
num = 30
suma = 30

def mouse():
    p = win.getMouse()
    x = p.x
    y = p.y
    print(y," y")
    print(x," x")

def st_1():
    global color
    for i in range(10):
        if color == "white":
            color = "black"
        elif color == "black":
            color = "white"

def st_2():
    global color
    global num
    global suma
    for i in range(100):
        if color == "white":
            num -= 1
            print(num," white")
        else:
            suma -= 1
            print(suma," black")
        time.sleep(1)

thread_st_1 = threading.Thread(target=st_1, args=())
thread_st_2 = threading.Thread(target=st_2, args=())
#thread_st_1.daemon = True
#thread_st_2.daemon = True
thread_st_1.start()
thread_st_2.start()
#thread_st_1.join()
#thread_st_2.join()
#while True:
  # print(mouse())


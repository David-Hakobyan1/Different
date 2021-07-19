import os
from graphics import *
import time
win=GraphWin("find",600,400)
path = raw_input("path: ")
name = raw_input("name: ")
def find(f_path, f_name):
    ls = os.listdir(f_path)
    x1,x2=0,0
    for f in ls:
        if os.path.isdir(f_path + "/" + f):
            find(f_path + "/" + f, f_name)
        elif f == f_name:
            ds=f_path + "/" +f
            t=Text(Point(300,200),ds)
            t.draw(win)
            x2+=1
            time.sleep(3)
            if x2>x1:
                t.undraw()
find(path, name)



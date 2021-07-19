from graphics import *
import time

win = GraphWin("chichu", 800, 600)
x = 400
y = 300
x1 = 410
y1 = 310
rect1 = Rectangle(Point(50,50),Point(750,550))
rect1.draw(win)
start =  Rectangle(Point(600,550),Point(750,600))
start.draw(win)
text = Text(Point(670,575),"start")
text.setSize(30)
text.setFill("green")
text.draw(win)
stop = Rectangle(Point(50,550),Point(200,600))
stop.draw(win)
text1 = Text(Point(130,575),"stop")
text1.setFill("green")
text1.setSize(30)
text1.draw(win)
qar = Rectangle(Point(200,200),Point(210,210))
qar.draw(win)
rect = Rectangle(Point(x,y),Point(x1,y1))
rect.draw(win)

def Mouse():
    p = win.getMouse()
    x1 = p.x
    y1 = p.y
    print(x1,y1)
    return x1,y1

def start():
    x,y = Mouse()
    if 559 <x< 751 and 549 <y< 601:
        print("start")
        return True
    else:
        print("sxal")
        return False

def stop():
    x,y = Mouse()
    if 49 <x< 201 and 550 <y< 601:
        print("stop")
        return True
    else:
        print("sxal")
        return False
speed = 0.5
if start():
    x,x1 = 400,410
    c = 0
    while True:
        klavish = win.getKey()
        rect.undraw()
        rect = Rectangle(Point(x,y),Point(x1,y1))
        rect.draw(win)
        if klavish == "s":
            while True:
                if klavish == "s":
                    rect.move(0,10)
                if klavish == "w":
                    rect.move(0,-10)
                if klavish == "a":
                    rect.move(-10,0)
                if klavish == "d":
                    rect.move(10,0)
                tmp = win.checkKey()
                if tmp:
                    klavish = tmp
                print(klavish)
                time.sleep(speed)            

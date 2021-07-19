# MODULE CONNECTION #
import graphics
import time

# VARIABLES,GRAPHIC OBJECT,IMAGE,TEXT #
win = graphics.GraphWin("chess", 800, 700)
win.setBackground("blue")
download_image = graphics.Image(graphics.Point(400, 400), "/home/David/Desktop/chess.png")
download_image.draw(win)
time.sleep(2)
msg = graphics.Text(graphics.Point(400,50),"D A V I D \n C H E S S")
msg.setTextColor("black")
msg.setSize(20)
msg.setStyle("bold italic")
msg.draw(win)
time.sleep(2)
msg.undraw()
sms = graphics.Text(graphics.Point(400,50),"W E L C O M E")
sms.setTextColor("red")
sms.setSize(20)
sms.setStyle("bold italic")
sms.draw(win)
time.sleep(2)
sms.undraw()
num = graphics.Text(graphics.Point(400,50),"GO! GO! GO!")
num.setTextColor("cyan")
num.setSize(30)
num.setStyle("bold italic")
num.draw(win)
time.sleep(1)
num.undraw()
download_image.undraw()

#CHESS TABLE#
def chess_table():
    x,y=0,100
    x1,y1=0,150
    for j in range(8):
        y+=50
        y1+=50
        x=150
        x1=200
        if j%2==0:
            for i in range(8):
                x+=50
                x1+=50
                rect = graphics.Rectangle(graphics.Point(x,y) ,graphics.Point(x1,y1))
                if i%2==0:
                    rect.setFill("white")
                    rect.draw(win)
                else:
                    rect.setFill("black")
                    rect.draw(win)
        elif j%2!=0:
            for i in range(8):
                x+=50
                x1+=50
                rect = graphics.Rectangle(graphics.Point(x,y), graphics.Point(x1,y1))
                if i%2==0:
                    rect.setFill("black")
                    rect.draw(win)
                else:
                    rect.setFill("white")
                    rect.draw(win)

chess_table()
time.sleep(1)



tiv = graphics.Text(graphics.Point(190,350),"8\n\n7\n\n6\n\n5\n\n4\n\n3\n\n2\n\n1")
tiv.setSize(16)
tiv.setTextColor("black")
tiv.draw(win)
tiv1 = graphics.Text(graphics.Point(610,350),"8\n\n7\n\n6\n\n5\n\n4\n\n3\n\n2\n\n1")
tiv1.setSize(16)
tiv1.setTextColor("black")
tiv1.draw(win)
ta = graphics.Text(graphics.Point(400,565),"a      b      c      d       e      f       g       h")
tar = graphics.Text(graphics.Point(400,135),"a      b      c      d       e      f       g       h")
ta.setTextColor("black")
tar.setTextColor("black")
ta.setSize(15)
tar.setSize(15)
ta.setStyle("bold italic")
tar.setStyle("bold italic")
ta.draw(win)
tar.draw(win)
time.sleep(1)


# NAME FIGUR, POSITION AND LOCATION  #

wrook = graphics.Image(graphics.Point(225,525), "/home/David/Desktop/wrook.png")
wrook1 = graphics.Image(graphics.Point(575,525), "/home/David/Desktop/wrook.png")
brook = graphics.Image(graphics.Point(225,175), "/home/David/Desktop/brook.png")
brook1 = graphics.Image(graphics.Point(575,175), "/home/David/Desktop/brook.png")
wrook.draw(win)
wrook1.draw(win)
brook.draw(win)
brook1.draw(win)
#time.sleep(1)
wknight = graphics.Image(graphics.Point(275,525), "/home/David/Desktop/wknight.png")
wknight1 = graphics.Image(graphics.Point(525,525), "/home/David/Desktop/wknight.png")
bknight = graphics.Image(graphics.Point(275,175), "/home/David/Desktop/bknight.png")
bknight1 = graphics.Image(graphics.Point(525,175), "/home/David/Desktop/bknight.png")
wknight.draw(win)
wknight1.draw(win)
bknight.draw(win)
bknight1.draw(win)
#time.sleep(1)
wbishop = graphics.Image(graphics.Point(325,525), "/home/David/Desktop/wbishop.png")
wbishop1 = graphics.Image(graphics.Point(475,525), "/home/David/Desktop/wbishop.png")
bbishop = graphics.Image(graphics.Point(325,175), "/home/David/Desktop/bbishop.png")
bbishop1 = graphics.Image(graphics.Point(475,175), "/home/David/Desktop/bbishop.png")
wbishop.draw(win)
wbishop1.draw(win)
bbishop1.draw(win)
bbishop.draw(win)
#time.sleep(1)
wking = graphics.Image(graphics.Point(425,525), "/home/David/Desktop/wking.png")
bking = graphics.Image(graphics.Point(425,175), "/home/David/Desktop/bking.png")
wking.draw(win)
bking.draw(win)
wquen = graphics.Image(graphics.Point(375,525), "/home/David/Desktop/wquen.png")
bquen = graphics.Image(graphics.Point(375,175), "/home/David/Desktop/bquen.png")
wquen.draw(win)
bquen.draw(win)
pawn = graphics.Image(graphics.Point(0,0), "/home/David/Desktop/pawn_black.png")
pawn.draw(win)
#time.sleep(1)

win.setBackground("silver")



# BLACK PAWN POSITION  RANGE #
q = 113
r = 113
for i in range(8):
    bpawn = graphics.Image(graphics.Point(q,r), "/home/David/Desktop/pawn_black.png")
    bpawn.draw(win)
    bpawn.move(q,r)
    q+=25



# WHITE PAWN POSITION RANGE #
q1 = 113
r1 = 238
for j in range(8):
    wpawn = graphics.Image(graphics.Point(q1,r1), "/home/David/Desktop/wpawn.png")
    wpawn.draw(win)
    wpawn.move(q1,r1)
    q1+=25



# SELECT THE PLACE THE FIGURE,WITH THE MOUSE #
def rectangle(x,y):
    column = 0
    for i in range(200,600,50):
        if x > i:
            column+=1
    row = 0
    for j in range(150,550,50):
        if y > j:
            row+=1
    return(column,row)
x,y = 0,0
x1,y1 = 0,0
x2,y2 = 0,0
while True:
    p = win.getMouse()
    x1 = p.getX()
    y1 = p.getY()
    if x1 > 199 and x1 < 601 and y1 > 149 and y1 < 551:
        print("chisht e")
        print(x)
        print(y)
        print(x1)
        print(y1)
        print(x2)
        print(y2)
        column,row=rectangle(x1,y1)
        x2 = (200+column*50)-25
        y2 = (150+row*50)-25
        x = x2 - x
        y = y2 - y
        pawn.move(x,y)
        x,y = x2,y2
    else:
        print("sxal e")
        print(x1)
        print(y1)

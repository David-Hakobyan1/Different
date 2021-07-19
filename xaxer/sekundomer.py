from graphics import *
import time
win = GraphWin("secundomer",600,400)
win.setBackground("black")
hashvark=0
milisecound=0
secound=0
minut=0
chas=0
jam=Text(Point(250,200),"00")
jam.setTextColor("red")
jam.draw(win)
rope=Text(Point(300,200),"00")
rope.setTextColor("green")
rope.draw(win)
vayrkyan=Text(Point(350,200),"00")
vayrkyan.setTextColor("white")
vayrkyan.draw(win)
while hashvark<75700:
    hashvark+=1
    if hashvark == 75700:
        milisecound+=1
        hashvark=0
        if milisecound==60:
            secound+=1
            hashvark=0
            milisecound=0
            if secound<10:
                vayrkyan.undraw()
                vayrkyan.draw(win)
                vayrkyan.setText("0"+str(secound))
            if secound>=10:
                vayrkyan.undraw()
                vayrkyan.draw(win)
                vayrkyan.setText(secound)
            if secound==60:
                minut+=1
                secound=0
                milisecound=0
                hashvark=0
                vayrkyan.undraw()
                vayrkyan.draw(win)
                vayrkyan.setText("00")
                if minut<10:
                    rope.undraw()
                    rope.draw(win)
                    rope.setText("0"+str(minut))
                if minut>=10:
                    rope.undraw()
                    rope.draw(win)
                    rope.setText(minut)
                if minut==60:
                    rope.undraw()
                    rope.draw(win)
                    rope.setText("00")
                    chas+=1
                    minut=0
                    hashvark=0
                    secound=0
                    milisecound=0
                    if chas<10:
                        jam.undraw()
                        jam.draw(win)
                        jam.setText("0"+str(chas))
                    if chas>=10:
                        jam.undraw()
                        jam.draw(win)
                        jam.setText(chas)
                    if chas==24:
                        jam.undraw()
                        jam.draw(win)
                        jam.setText("00")
                        hashvark=0
                        milisecound=0
                        secound=0
                        minut=0
                        chas=0
                    
                               

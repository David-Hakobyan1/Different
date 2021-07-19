import graphics
import time
import math
win = graphics.GraphWin("kalkulyator",400,400)
win.setBackground("gray")
x,x1=0,50
y,y1=50,100
nor=""
st=""
for i in range(4):
    y+=50
    y1+=50
    x=0
    x1=50
    if i%2==0 or i%2!=0:
        for j in range(4):
            x+=50
            x1+=50
            rect=graphics.Rectangle(graphics.Point(x,y),graphics.Point(x1,y1))
            rect.draw(win)
z=75
h=125
n=1
arajin = 0
yerkrord = 0
ardyunq = 0
gorcoxutyun = ""
glo=250
glo1=80
suma=""
ekr=graphics.Text(graphics.Point(glo,glo1),suma)
ekr.draw(win)
while True:
    if z<200 and h==125:
       tiv=graphics.Text(graphics.Point(z,h),n)
       tiv.draw(win)
       z+=50
       n+=1
    elif z==225 and h==125:
       tiv=graphics.Text(graphics.Point(z,h),"/")
       tiv.draw(win)
       h+=50
       z=75
       n=4
    elif h==175 and z<225:
       tiv=graphics.Text(graphics.Point(z,h),n)
       tiv.draw(win)
       z+=50
       n+=1
    elif z==225 and h==175:
       tiv=graphics.Text(graphics.Point(z,h),"*")
       tiv.draw(win)
       z=75
       n=7
       h+=50
    elif z<225 and h==225:
        tiv=graphics.Text(graphics.Point(z,h),n)
        tiv.draw(win)
        z+=50
        n+=1
    elif z==225 and h==225:
        tiv=graphics.Text(graphics.Point(z,h),"-")
        tiv.draw(win)
        z=75
        h+=50
        n=0
        t="="
    elif z<225 and h==275:
        tiv=graphics.Text(graphics.Point(z,h),n)
        tiv.draw(win)
        z+=50
        miv=graphics.Text(graphics.Point(z,h),t)
        miv.draw(win)
        z+=50
        liv=graphics.Text(graphics.Point(z,h),".")
        liv.draw(win)
        z+=50
        niv=graphics.Text(graphics.Point(z,h),"+")
        niv.draw(win)
    elif z==225:
        while True:
            p=win.getMouse()
            x2=p.getX()
            y2=p.getY()
            if x2>49 and x2<101 and y2>99 and y2<151:
                k=1
                print(k)
            elif x2>100 and x2<151 and y2>99 and y2<151:
                k=2
                print(k)
            elif x2>150 and x2<201 and y2>99 and y2<151:
                k=3
                print(k)
            elif x2>200 and x2<251 and y2>99 and y2<151:
                k="/"
                print(k)
            elif x2>49 and x2<101 and y2>149 and y2<201:
                k=4
                print(k)
            elif x2>99 and x2<151 and y2>149 and y2<201:
                k=5
                print(k)
            elif x2>149 and x2<201 and y2>149 and y2<201:
                k=6
                print(k)
            elif x2>199 and x2<251 and y2>149 and y2<201:
                k="*"
                print(k)
            elif x2>49 and x2<101 and y2>199 and y2<251:
                k=7
                print(k)
            elif x2>99 and x2<151 and y2>199 and y2<251:
                k=8
                print(k)
            elif x2>149 and x2<201 and y2>199 and y2<251:
                k=9
                print(k)
            elif x2>199 and x2<251 and y2>199 and y2<251:
                k="-"
                print(k)
            elif x2>49 and x2<101 and y2>249 and y2<301:
                k=0
                print(k)
            elif x2>99 and x2<151 and y2>249 and y2<301:
                k="="
                print(k)
            elif x2>149 and x2<201 and y2>249 and y2<301:
                k="."
                print(k)
            elif x2>199 and x2<251 and y2>249 and y2<301:
                k="+"
                print(k)
            else:
                print("sxal mutqagrum")
            suma+=str(k)
            ekr.setText(suma)
            if k==1 or k==2 or k==3 or k==4 or k==5 or k==6 or k==7 or k==8 or k==9 or k==0 or k==".":
                nor += str(k)
                if gorcoxutyun == "":
                    arajin = float(nor)
                else:
                    yerkrord = float(nor)
            if k=="+" or k=="-" or k=="*" or k=="/":
                nor = ""
                gorcoxutyun = k
                st+=k
            if k == "=" and st=="+":
                ardyunq = arajin + yerkrord
                print(ardyunq)
                ekr.undraw()
                ekr.draw(win)
                ekr.setText(str(ardyunq))
                gorcoxutyun=""
                suma=""
                st=""
                nor=""
            if k == "=" and st=="-":
                ardyunq = arajin - yerkrord
                print(ardyunq)
                ekr.undraw()
                ekr.draw(win)
                ekr.setText(str(ardyunq))
                gorcoxutyun=""
                suma=""
                st=""
                nor=""
            if k == "=" and st=="*":
                ardyunq = arajin * yerkrord
                print(ardyunq)
                ekr.undraw()
                ekr.draw(win)
                ekr.setText(str(ardyunq))
                gorcoxutyun=""
                suma=""
                st=""
                nor=""
            if k == "=" and st=="/":
                ardyunq = arajin / yerkrord
                print(ardyunq)
                ekr.undraw()
                ekr.draw(win)
                ekr.setText(str(ardyunq))
                gorcoxutyun=""
                suma=""
                st=""
                nor=""

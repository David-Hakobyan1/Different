import random
#import graphics
#import time

#win = graphics.GraphWin("POLE CHUDES",600,600)
#win.setBackground("cyan")
#f=open("file.txt")
#smb=f.read().strip()
#split1=smb.split(",")
#patahakan=random.randrange(0,len(split1))
#bar=split1[patahakan]

#def patker():
 #   x=0
  #  x1=50
   # for i in range(len(bar)):
    #    y=150
#        y1=200
 #       x+=50
  #      x1+=50
  #      rect=graphics.Rectangle(graphics.Point(x,y),graphics.Point(x1,y1))
   #     rect.draw(win)
#patker()
#y=175
#ci=0
#while True:
 #   x=25
 #   bol=False
  #  if ci!=len(bar):
   #     gto=raw_input("mutq tar :")
    #    for j in bar:
     #       x+=50
      #      if gto==j:
       #         ci+=1
        #        bol=True
         #       ect=graphics.Text(graphics.Point(x,y),j)
          #      ect.setSize(20)
           #     ect.setTextColor("black")
            #    ect.setStyle("bold italic")
             #   ect.draw(win)

#        if not bol:
 #           print("sxal mutq !!!")
  #          ct=graphics.Text(graphics.Point(100,125),"sxal Tar !!!")
   #         ct.setSize(20)
    #        ct.setTextColor("red")
     #       ct.setStyle("bold italic")
      #      ct.draw(win)
       #     time.sleep(1)
        #    ct.undraw()
#    else:
 #       print("avart")
  #      time.sleep(3)
   #     break



# POLE CHUDES )))
def pole():
    f = open('file.txt')
    smb = f.read().strip()
    split1 = smb.split(",")
    patahakan = random.randrange(0, len(split1))
    bar = split1[patahakan]
    astx = []
    
    for j in bar:
        astx.append("*")  
    print(astx)
    return bar,astx
bar,astx=pole()
ci=0    
while True:
    bol=False
    if ci!=len(bar):
        count = 0   
        mutq = raw_input("mutq tar :")
        for i in bar:
            if i == mutq:
                ci+=1
                astx[count] = i
                bol=True
            count+=1
        print(astx)
        if not bol:
            print("sxale")
    else: 
        print("avart")
        ci=0
        bar,astx=pole()        


        

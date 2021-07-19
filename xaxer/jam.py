import math
import time

from tkinter import *
root = Tk()
canvas = Canvas(root, width = 500, height = 550)
canvas.pack()
canvas.create_oval(10, 10, 490, 490, fill = "lightblue")
canvas.create_text(250, 350, text = 'na Python', font = ('Arial', 8))
canvas.create_text(250, 225, text = '.', font = ("Arial", 62))
i = 0
while i < 60:
    i+=1
    canvas.create_line(250 + 210 * math.cos(-i * 6 * math.pi/180 + math.pi/2),
                       250 - 210 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                       250 + 190 *     math.cos(-6 * i * math.pi/180 + math.pi/2),
                       250 - 190 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                       width = 2)
        
    
    if i % 5 == 0:
         canvas.create_line(250 + 215 * math.cos(-i * 6 * math.pi/180 + math.pi/2),
                            250 - 215 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                            250 + 190 * math.cos(-6 * i * math.pi/180 + math.pi/2),
                            250 - 190 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                            width = 4)
         continue
i = 0
while i < 12:
    i += 1
    canvas.create_text(250 + 225 * math.cos(-i * 30 * math.pi/180 + math.pi/2),
                       250 - 225 * math.sin(-30 * i * math.pi/180 + math.pi/2),
                       text = i, font = ('Arial' ,16))
    

i = 950
while 1:
    time_now = time.localtime()
    time_sec = int(time.strftime("%S", time_now))
    time_hour = int(time.strftime("%I", time_now))
    time_min = int(time.strftime("%M", time_now))
    sec_angle = 6 * time_sec
    min_angle = time_min * 6 + time_sec * 0.1
    hour_angle = time_hour * 30 + time_min * 60 * (30/3600)
    line_min = canvas.create_line(250, 
                                  250,
                                  250 - 180 * math.cos(min_angle * math.pi/180 + math.pi/2),
                                  250 - 180 * math.sin(min_angle * math.pi/180 + math.pi/2),                                                                                       width = 3, fill = 'darkblue')
    line_hour = canvas.create_line(250,
                                   250,
                                   250 - 150 * math.cos(hour_angle * math.pi/180 + math.pi/2),
                                   250 - 150 * math.sin(hour_angle * math.pi/180 + math.pi/2),
                                   width = 5, fill = 'darkblue')
    line_sec = canvas.create_line(250,
                                  250,
                                  250 - 180 * math.cos(sec_angle * math.pi/180 + math.pi/2),
                                  250 - 180 * math.sin(sec_angle * math.pi/180 + math.pi/2),                                                                                       width =2, fill = 'red')
    text_bottom = canvas.create_text(i, 525, 
                                     text = 'DAVID'+
                                     ' HAKOBYAN ', font = ('Arial',16))
    i = i - 0.5
    if i == -600:
        i = 950
    root.update()
    canvas.delete(line_sec)
    canvas.delete(line_min)
    canvas.delete(line_hour)
    canvas.delete(text_bottom)
root.mainloop
 

# Milionater Xax

#####################################################################################
#IMPORT: Tkinter, sys, random, time
#FUNCTION: open_file,filter_file, act, questions_answers_on_the_screen, quit, main
#BRIEF:
#PARAMS: 
#OUTPUT:
#RETURN: 
#####################################################################################

from Tkinter import*
import sys
import random
import time

root = Tk()
root.title("grafic program")
root.geometry("1400x800")
canv = Canvas(bg='yellow')
canv.pack(fill=BOTH,expand=1)


#checking for file existence
def open_file():
    try:
        with open("files.txt") as f:
            return f.read()
    except FileNotFoundError:
        print("no such file files.txt")
        sys.exit()


#get the elements of the file
def filter_file(my_file):
    st = ""
    l = []
    for el in my_file:
        if el != "\n":
            st+=el
        else:
            lis = st.split(":")
            l.append(lis)
            st = ""
    return l


#check for correct answer
def act(h,p,f,t):
    if h==p:
        for i in range(len(f)):
            if h in f[i]:
                f.pop(i)
                canv.delete(t)
                questions_answers_on_the_screen(f)
                
    else:
        canv.create_text(680,350,text="Sxal patasxan!!! Xaxi avart",fill="red",font=("Times",30))
        time.sleep(2)
        quit()


#shielding questions and answers
def questions_answers_on_the_screen(filtered_file):
    if len(filtered_file)!=0:
        s = random.randrange(len(filtered_file))
        filters = filtered_file[s][1].split(",")
        texts = canv.create_text(650,300,text=filtered_file[s][0],fill="blue",font=("Times",30))
        c=0
        for el in filters:
            if c==0:
                btn1 = Button(text=el, background="#555", foreground="#ccc", padx="170", pady="14", font="13", command=lambda: act(filters[0],filtered_file[s][2],filtered_file,texts))
                btn1.place(x=125,y=550)
            if c==1:
                btn2 = Button(text=el, background="#555", foreground="#ccc", padx="170", pady="14", font="13", command=lambda: act(filters[1],filtered_file[s][2],filtered_file,texts))
                btn2.place(x=125,y=650)
            if c==2:
                btn3 = Button(text=el, background="#555", foreground="#ccc", padx="170", pady="14", font="13", command=lambda: act(filters[2],filtered_file[s][2],filtered_file,texts))
                btn3.place(x=750,y=550)
            if c==3:
                btn4 = Button(text=el, background="#555", foreground="#ccc", padx="170", pady="14", font="13", command=lambda: act(filters[3],filtered_file[s][2],filtered_file,texts))
                btn4.place(x=750,y=650)
            c+=1
    else:
        canv.create_text(680,350,text="Xaxi avart,duq patasxanel eq bolor harcerin",fill="red",font=("Times",30))
        time.sleep(2)
        quit()


#function quit
def quit():
    root.quit()


#call main
def main():
    my_file = open_file()
    filtered_file = filter_file(my_file)
    q_a_screen = questions_answers_on_the_screen(filtered_file)
    mainloop()


#check main
if __name__ == "__main__":
    main()

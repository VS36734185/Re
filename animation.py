from tkinter import * 
from random import choice, randint 
import time
root = Tk() 
root.title('Экзамен') 
root.geometry('500x500') 
root.resizable(width=False, height=False) 
cnv = Canvas(root,width = 500,height = 500,bg = "green")
cnv.pack()
sq = cnv.create_oval (200,150,200+150,150+100,fill = "white")
speede = -2
speeds = -1
sr = cnv.create_oval(223,211,223+100,211+100,fill = "red")
speedx = 2
speedy = 3
while True:
    root.update()
    root.update_idletasks()
    time.sleep(1/10) 
    cnv.move(sr,speedx,speedy) 
    cnv.move(sq,speede,speeds)
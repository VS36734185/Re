from tkinter import *
from random import choice, randint  
import time
class Ball:
    def __init__ (self):
        self.form = cnv.create_oval (200,150,200+30,150+30,fill = "lime")
        self.speedx = 3
        self.speedy = 2
    def move (self):
        cnv.move(self.form,self.speedx,self.speedy)
        x1,y1,x2,y2 = cnv.coords(self.form)
        if x2 <=0:
            rck2.add_score("right")
            cnv.delete(self.form)
            self.__init__()
        elif x1 >= 500:
            rckt.add_score("left")
            cnv.delete(self.form)
            self.__init__()
        if y1<=0 or y2>= 500:
             self.speedy = -self.speedy
        xw1,yw1,xw2,yw2 = cnv.coords(rckt.form)
        if xw2 >=x1 and xw1 <=x2 and yw2 >=y1 and yw1 <=y2:
             self.speedx = -self.speedx
        xw1,yw1,xw2,yw2 = cnv.coords(rck2.form)
        if xw2 >=x1 and xw1 <=x2 and yw2 >=y1 and yw1 <=y2:
             self.speedx = -self.speedx
root = Tk() 
root.title('Экзамен') 
root.geometry('500x500') 
root.resizable(width=False, height=False) 
cnv = Canvas(root,width = 500,height = 500,bg = "green")
cnv.pack()
ex = Ball()
class Raketka:   
    def __init__ (self):
        self.form = cnv.create_rectangle (30,90,30+20,90+120,fill = "red")
        self.speedx = 0
        self.speedy = 0    
        self.score = 0
    def add_score(self, side):
        if side == "right":
            print( "(правый) забивает очко!")
            self.score += 1
        elif side == "left":
            print("(левый) забивает очко!")
            self.score += 1
    def get_score(self):
        return self.score
    def move (self):
        x1,y1,x2,y2 = cnv.coords(self.form)
        if y1 + self.speedy<=0 or y2+self.speedy>= 500:
             self.speedy = 0
        cnv.move(self.form,self.speedx,self.speedy) 
    def control (self,event):
        if event.keysym == "w":
            self.speedy = -8
        elif event.keysym =="s":
            self.speedy = 8 
    def stop (self,event):
        if event.keysym =="w" or event.keysym == "s":
            self.speedy = 0
rckt = Raketka()
root.bind_all("<KeyPress>",rckt.control,add = "+")
root.bind_all("<KeyRelease>",rckt.stop,add = "+")
     
class raketka2:   
    def __init__ (self):
        self.form = cnv.create_rectangle (470,90,470-20,90+120,fill = "black")
        self.speedx = 0
        self.speedy = 0
        self.score = 0

    def hit_ball(self, ball_position):
        if ball_position == "left_wall":
            self.add_score("right")
        elif ball_position == "right_wall":
            self.add_score("left")

    def add_score(self, side):
        if side == "right":
            print( "(правый) забивает очко!")
            self.score += 1
        elif side == "left":
            print( "(левый) забивает очко!")
            self.score += 1
    def get_score(self):
        return self.score
    def move (self):
        x1,y1,x2,y2 = cnv.coords(self.form)
        if y1 + self.speedy<=0 or y2+self.speedy>= 500:
             self.speedy = 0
        cnv.move(self.form,self.speedx,self.speedy)   
    def control (self,event):
        if event.keysym == "Up":
            self.speedy = -6
        elif event.keysym == "Down":
            self.speedy = 6
    def stop (self,event):
        if event.keysym == "Up" or event.keysym == "Down":
            self.speedy = 0
rck2 = raketka2()
root.bind_all("<KeyPress>",rck2.control,add = "+")
root.bind_all("<KeyRelease>",rck2.stop,add = "+")

while True:
    root.update()
    root.update_idletasks()
    time.sleep(1/60) 
    ex.move()
    rckt.move()
    rck2.move()
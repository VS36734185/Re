import  tkinter as tk 
w = tk.Tk()
w.geometry("800x700")
w["bg"] = "green"
v  = "black"
r  = 144
f = "line2"
cnv = tk.Canvas(w,width = 720,height = 700,bg = "white")
cnv.grid(row = 0,column = 0,rowspan = 8)
def s (form): 
     global f
     f = form
def p(event):

   print (event) 
   if  f == "circle":
      cnv.create_oval(event.x-r,event.y-r,event.x+r,event.y+r,fill = v,outline = v)
   elif f == "rectangle":
       cnv.create_rectangle(event.x-r,event.y-r,event.x+r,event.y+r,fill = v,outline = v)     
   elif f == "line1":
      cnv.create_line(event.x-r,event.y-r,event.x+r,event.y+r,fill = v)
   elif f == "line2":
      cnv.create_line(event.x+r,event.y-r,event.x-r,event.y+r,fill = v)
      
k = tk.Button(w,text = "🟩",font = ("arial",30),fg = "green",bg = "white",command  =  lambda: s ("rectangle"),width = 3)
k.grid(row = 0,column = 1)


k = tk.Button(w,text = "🟢",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 1,column = 1)


k = tk.Button(w,text = "\\\\",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 2,column = 1)

k = tk.Button(w,text = "//",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 3,column = 1)

k = tk.Button(w,text = "➖",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 4,column = 1)

k = tk.Button(w,text = "➕",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 5,column = 1)

k = tk.Button(w,text = "❌",font = ("arial",30),fg = "green",bg = "white",command  = None,width = 3)
k.grid(row = 6,column = 1)

k = tk.Button(w,text =  r,font = ("arial",30),fg = v,bg = "white",command  = None,width = 3)
k.grid(row = 7,column = 1)

w.bind_all("<1>",p)




















tk.mainloop()


          

 
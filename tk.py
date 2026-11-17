import tkinter as tk
def fun():
    txt.configure(text = "bye")
w = tk.Tk()
w.geometry("800x600")
w["bg"] = "white"

txt = tk.Label(w,text = "hello",font = ("arial",50),fg = "green",bg = "white")
txt.pack()
k = tk.Button(w,text = "hello",font = ("arial",50),fg = "green",bg = "white",command  = fun)
k.pack()














tk.mainloop()
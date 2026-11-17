from tkinter import * 
from random import choice, randint 

root = Tk() 
root.title('Экзамен') 
root.geometry('500x500') 
root.resizable(width=False, height=False) 

number1 = randint(1, 1000) 
number2 = randint(1, 1000) 
correct_answer = number1 + number2 

label = Label(root, text=f'Сколько будет {number1} + {number2}?') 
label.pack() 

def check_answer(button): 
    if int(button['text']) == correct_answer: 
        print('Молодец!') 
    else: 
        print('Неправильно!') 

buttons = [] 
for i in range(4): 
    button = Button(root, font='5', width=15, height=1, command=lambda b=button: check_answer(b)) 
    button.place(x=160, y=130 + i * 70) 
    buttons.append(button) 

answers = [correct_answer] 
while len(answers) < 4: 
    false_answer = randint(1, 2000) 
    if false_answer not in answers: 
        answers.append(false_answer) 

for button, answer in zip(buttons, answers): 
    button['text'] = str(answer) 

root.mainloop()
from tkinter import *
 
root = Tk()
root.geometry("300x250")
 
canvas = Canvas(bg="white", width=250, height=200)
canvas.pack(anchor=CENTER, expand=1)
 
canvas.create_rectangle(10, 20, 200, 60, fill="#80CBC4", outline="#004D40")
 
root.mainloop()
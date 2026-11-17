
import faker
import random
import tkinter as tk

root = tk.Tk() 
root.title('6') 

label = tk.Label(root, text="Выберите режим")
label.grid(row=0, column=0, columnspan=3)

button_flip = tk.Button(root, text="переворот", width=10)
button_flip.grid(row=1, column=0)
button_shuffle = tk.Button(root, text="перемешивание", width=10)
button_shuffle.grid(row=2, column=0)
button_skip = tk.Button(root, text="пропуск буквы", width=10)
button_skip.grid(row=3, column=0)

label_mode = tk.Label(root, text="1")
label_mode.grid(row=0, column=3, columnspan=2)

label_word = tk.Label(root, text="", font=("Arial", 16))
label_word.grid(row=1, column=1, columnspan=2)

entry_answer = tk.Entry(root)
entry_answer.grid(row=2, column=1, columnspan=2)

result_label = tk.Label(root, text="", fg="red")
result_label.grid(row=4, column=0, columnspan=3)

f = faker.Faker("ru_RU")

current_word = ""

def flip_word_mode():
    global current_word
    current_word = f.word()
    challenge = current_word[::-1]
    label_word.config(text=challenge)
    result_label.config(text="")
    entry_answer.delete(0, tk.END)

def check_answer():
    answer = entry_answer.get()
    if answer == current_word:
        result_label.config(text="Вы угадали")
    else:
        result_label.config(text=f"Вы ошиблись. Правильный ответ: {current_word}")

button_flip.config(command=flip_word_mode)

button_send = tk.Button(root, text="Отправить", width=10, command=check_answer)
button_send.grid(row=3, column=1, columnspan=2)


















































































    
root.mainloop()
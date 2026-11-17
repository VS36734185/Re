import tkinter as tk
#Создание окна
import time
import random
root = tk.Tk() 
root.title('Мини пиццерия') 
root.geometry('800x600') 
root.resizable(width=False, height=False) 
cnv = tk.Canvas(root,width = 800,height =300,bg = "white")
cnv.grid(row = 0,column = 0,columnspan = 2)

class Pizza:
    def __init__ (self):
       #Создание пиццы
       rm = random.choice([40,60,80])
       print(rm)
       self.form = cnv.create_oval(150-rm,150-rm,150+rm,150+rm,fill = "lemon chiffon")
       self.speed = 0
       self.zakaz = cnv.create_text(150,150,text = "" )
       self.sp = []
       self.zakazlist = ["Соус"]+ create_zakaztext_buttons()
       self.createtext = cnv.create_text(400,20,text = self.zakazlist)
       print(self.zakazlist)
    def move(self):
     cnv.move(self.form,self.speed,0)
     cnv.move(self.zakaz,self.speed,0)
     spx = cnv.coords(self.form,)[0]
     if spx > root.winfo_width():
        cnv.delete(self.createtext)
        self.__init__()

def create_zakaztext_buttons():
  pizzazakz = []
  #Создание заказа
  rew = ["Соус", "Пепперони", "Курица", "Сыр", "Грибы","Колбаски"]
  random_rand = random.randint(1,5)
  print(f"Заказ {random_rand}")
  for i in range(random_rand):
    random_ingredient = random.choice(rew)
    pizzazakz.append(random_ingredient)
  return pizzazakz
ex = Pizza()
    
    
#Кнопка для выбора ингредиентов
def create_ingredient_buttons(ingredients, button_list):
    num = 1
    for ingredient in ingredients:
        button = tk.Button(root, text=ingredient, command=lambda i=ingredient: ingredient_clicked(i))
        button.grid(row = num,column = 0 ) 
        num = num + 1
        button_list.append(button)
#функция кнопки ингредиентов
def ingredient_clicked(ingredient):
    ex.sp.append(ingredient)
    cnv.itemconfig(ex.zakaz,text ="\n".join (ex.sp))
    print(f"Выбран ингредиент: {ingredient}")
ingredients = ["Соус", "Пепперони", "Курица", "Сыр", "Грибы","Колбаски"]
ingredient_buttons = [] 

create_ingredient_buttons(ingredients, ingredient_buttons)
#Функция для кнопки готово
def finish_selection():
    print(ex.sp)
    if "Соус" in ex.sp:
        ex.speed = 4
        print("Пицца отправляется в печь")
    else:
        "Соус" not in ex.sp
        print("На пицце нет соуса! Добавьте Соус перед тем,как отправить в печь")


   #Пересоздать пиццу ex.__init__()
    print("Выбор завершен!")
finish_button = tk.Button(root, text = "В печь", command=finish_selection)

finish_button.grid(row = 1,column = 1)

while True:
 root.update()
 root.update_idletasks()
 ex.move()
 time.sleep(1/60)
 
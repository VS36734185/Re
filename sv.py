import pyautogui as pyg
import time

def screen():
    time.sleep(6)
    cord1 = pyg.position()
    print(cord1)
    time.sleep(6)
    cord2 = pyg.position() 
    print(cord2)
    width = (cord2.x - cord1.x)
    height = (cord2.y - cord1.y)
    print(f"Ширина :{width},| Высота: {height}")
    pyg.screenshot("screenshot.png",region = (cord1.x, cord1.y,width,height))
    print("Cкриншот сохранен как screenshot.png")
#screen()    
def poisk():
    obl = pyg.locateOnScreen("Screenshot.png")
    if obl is None:
        print("Кнопка не найдена на экране!")
        return
    x,y = pyg.center(obl)
    pyg.click(x,y)
time.sleep(6) 
poisk()

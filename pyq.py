import pyautogui as pyg
import time

time.sleep(6)
poz = pyg.position()
print(poz)
pyg.moveTo(239,160,duration = 3)
# pyg.click(clicks = 2)
# pyg.moveRel(200,232,duration = 2)
#pyg.dragRel(150,0,duration = 6)
#pyg.dragRel(0,150,duration = 1)
#pyg.dragRel(-150,0,duration = -6)
#pyg.dragRel(0,-150,duration = -1)
def draw_cube(x,y,size):
    pyg.moveTo(x, y)
    
    pyg.dragRel(size, 0, duration=0.1)  # Вправо
    pyg.dragRel(0, size, duration=0.1)  # Вниз
    pyg.dragRel(-size, 0, duration=0.1) # Влево
    pyg.dragRel(0, -size, duration=0.1) # Вверх

    # Рисуем верхнюю грань
    pyg.dragRel(size // 2, -size // 2, duration=0.1) # Вправо-вверх
    
    pyg.dragRel(size, 0, duration=0.1)  # Вправо
    pyg.dragRel(0, size, duration=0.1)  # Вниз
    pyg.dragRel(-size, 0, duration=0.1) # Влево
    pyg.dragRel(0, -size, duration=0.1) # Вверх
    pyg.dragRel(0,size,duration = 0.1)
    

    pyg.dragRel(-size // 2, size // 2, duration=0.1) # Влево-вниз
    pyg.dragRel(size, 0, duration = 0.1)
    pyg.dragRel(size // 2,-size // 2,duration = -0.1)
    pyg.dragRel(0,-size,duration = 0.1)
    pyg.dragRel(-size // 2, size // 2, duration=0.1)

draw_cube(400,400,50)
  

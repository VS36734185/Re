import pyautogui as pyg
import time 
time.sleep(3)

pyg.press("enter")
pyg.write("'Hello,бWorld'\n" ,interval = 0.4)
'Hello,World'
with pyg.hold("shift"):
    pyg.write("and") 
    
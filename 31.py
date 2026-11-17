import random
import time 
magnat = ["бекон","паста","яйца"]
for br in range(3):
   print(random.choice(magnat))

it = input("на сколько заводить? ")
for vg in range(int(it)):
   print(f"осталось {int(it) - vg} секунд")
   time.sleep(1)
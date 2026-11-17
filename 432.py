import random
class RPG ():
    def __init__ (self,health,damage,name):  
          self.name = name
          self.health = health
          self.damage = damage
          print(f"у тебя {self.health} hp,{self.damage} dmg")
    def attack(self,name):
        name.health -= self.damage
        print(f"Вы нанесли урон,осталось {name.health}")
        if name.health <= 0:
            print("Бой окончен")
            return True
        return False
class VRG ():
    def __init__(self):
          rases = {"Эльф": (200,19),"Гном":(290, 15), 
"Человек": (250, 12)}
          self.name = random.choice(list(rases))
          self.health = rases[self.name][0]
          self.damage = rases[self.name][1]
          print(f"На тебя напал {self.name} {self.health} hp,{self.damage} dmg")
    def attack(self,name):
        name.health -= self.damage
        print(f"Вам нанесли урон,осталось {name.health}")
        if name.health <= 0:
            print("Бой окончен")
            return True
        return False
def start():
    print("Привет рпшник,приступай к игре")
    nme = input("введи свое имя? ")
    rases = {"Эльф": (200,19),"Гном":(290, 15), 
"Человек": (250, 12)}
    cvf = input("какой ты расы? ")
    cvf = "Гном"
    while  cvf not in rases:
      cvf = input("какой ты расы? ")
    print(cvf)
    hlth = rases[cvf][0]
    dmg = rases[cvf][1]
    return RPG(health = hlth,damage = dmg,name  =  nme)
    
def game():
    vrgs = VRG()
    tr = input("Готов сражаться? ")
    if tr == "Да":
        print("Начало боя")
        ft(vrgs)
    else:
        print("Побег")
        e = random.randint(0,100)
        if e <60:
           print("Побег успешный")
           game()
        if e>=60:
          print("Побег не удался")
          ft(vrgs)
def ft(vrag):
         res = rpg.attack(vrag)
         if res == False: 
            res = vrag.attack(rpg)
            if res == False:
                ft(vrag)
         else:
            game()
rpg = start()
game()

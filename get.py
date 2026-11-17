import requests as req

token = "5cc66b250623cfeb0c5fcd1d841b0cc3"

def gethero(heroid):
    url = f"https://superheroapi.com/api/{token}/{heroid}"
    response = req.get(url)
    hero = response.json()
    return hero

def war(id1, id2):
    her1 = gethero(id1)
    her2 = gethero(id2)
    
    name1 = her1["name"]
    name2 = her2["name"]
    print(f"Сравниваем: {name1} vs {name2}")
    
    powerstats = ["intelligence", "strength", "speed", "durability", "power", "combat"]
    score1 = 0
    score2 = 0
    
    for stat in powerstats:
        val1 = her1["powerstats"].get(stat)
        val2 = her2["powerstats"].get(stat)
        
      
        try:
            val1 = int(val1)
        except:
            val1 = 0
        try:
            val2 = int(val2)
        except:
            val2 = 0
        
        print(f"{stat.capitalize()}: {name1} = {val1} | {name2} = {val2}")
        
        if val1 > val2:
            score1 += 1
        elif val2 > val1:
            score2 += 1
    
    if score1 > score2:
        print(f"Победитель: {name1}")
    elif score2 > score1:
        print(f"Победитель: {name2}")
    else:
        print("Ничья!")

war(id1=5, id2=3)

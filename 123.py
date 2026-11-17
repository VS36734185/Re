to_buy = ["Молоко","Яйца","Cметана","Йогурт"]
print(to_buy)
stomp = to_buy[-3:] 
print(stomp)
to_buy.append("Вода")
print(to_buy)
shaurma = tuple(to_buy)
print(shaurma)
shaurma  = shaurma[0:4]+("Сок",)
print(shaurma)
text ="купить: " +" ".join(shaurma)
print(text)
text2 = text.split(":")
print(text2)

def water (a = 4,b = 60):
    otvet = a+b
    return otvet

a = input("какие числа? ")
a = int(a)

b = input("какие числа? ")
b = int(b)
#print(water(a,b))

def sergo (a):
    tomato = 0
    for slava in a:
        if slava  % 2 == 0:
            tomato +=1 
    
    return tomato 
dwq = [2,4,6]
print(sergo(a = dwq))
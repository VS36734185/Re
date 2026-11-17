def print_check(honey_positions):
    sum = 0
    print("ООО Медовый Гексагон\n")
    
    for honey in honey_positions:
        name = honey[0]
        amount = honey[1]
        price = honey[2]
        print(f"{name} ({amount} шт.) - {price} руб.")
        sum += amount * price  
    print(f"\nИтого: {sum} руб.")
    print("Спасибо за покупку!")

def decorator(func):
    def wrapper():
        print("Начало декоратор")
        func()
        print("Конец декоратор")
    return wrapper
@decorator
def main():
    print("Функция работае")
main()
def print_ingredients(ingredients):
    for ingredient in ingredients:
        print(ingredient)

# Декоратор, который добавляет "булочку" в начало и конец вывода
def bun_decorator(func):
    def wrapper(ingredients):
        print("Булочка сверху ")
        func(ingredients)
        print("Булочка снизу ")
    return wrapper

# Применение декоратора к функции
@bun_decorator
def print_ingredients(ingredients):
    for ingredient in ingredients:
        print(ingredient)

 #Вызов списком ингредиентов
ingredients_list = ["Лист салата", "Помидор", "Котлета", "Сыр"]
print_ingredients(ingredients_list)
import faker
f = faker.Faker("ru_RU")
print("Вы попали в игру в слова, в чате появится слово задом-наперед, ваша задача - отгадать слово")
print("Готовы")
i = input()
while True:
    print()
    words = f.word()
    print(words)
    pere = words[::-1]
    print(pere)
    lasla = input("--> ")
    if lasla == words:
        print("Вы угадали")
    else:
        print("Вы ошиблись")
        break
        


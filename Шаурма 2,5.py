
import s_taper, random, faker
from s_taper.consts import *
fake = faker.Faker("ru_RU")
shema = {
    "user_id": INT + KEY,
    "name": TEXT,
    "age": INT,
}
tabl = s_taper.Taper("users", "data.db").create_table(shema)
tabl.write([1, "Lasla", 18])
tabl.write([2, "Denis", 16])
users = tabl.read_all()
print(users[0][1], users[1][1])
print(users)
 
player = users[0][1]  # имя игрока берём из таблицы
print(f"Привет, {player}! Сыграем в игру.")
 
while True:
    secret = random.randint(1, 10)
    answer = input("Я загадал число от 1 до 10. Попробуй отгадать: ")
 
    if not answer.isdigit():
        print("Нужно прислать число. Попробуем ещё раз!")
        continue
 
    if int(answer) == secret:
        print(f"Поздравляю, {player}! Ты отгадал, это было число {secret}! ")
        break
    else:
        print(f"Не угадал, я загадывал {secret}. Загадываю другое число!")

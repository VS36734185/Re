import s_taper, random, faker, time
from s_taper.consts import *

fake = faker.Faker("ru_RU")


schema_players = {
    "id": INT + KEY,
    "name": TEXT,
    "age": INT,
    "premium": BLN,
}


players_table = s_taper.Taper("players", "data.db").create_table(schema_players)

#chet = 0
# for id in range(1, 201):
#     name = fake.user_name()
#     age = random.randint(10, 80)
#     premium = random.choice([True, False])
#     players_table.write([id, name, age, premium])

#players = players_table.read_all()
# chet = 0
# players = players_table.read_all()

# for player in players:
#     age = player[2]
#     premium = player[3]
    
#     if age < 25 and premium:
#         print(f"ID: {player[0]}, Имя: {player[1]}")
#         chet += 1

# print(f"Количество игроков младше 25 лет с премиум аккаунтом: {chet}")
# for player in players:
#     if player [2] >50:
#         chet +=1
        #print(player)
#print(players)
#print(chet)

#eight = players_table.read("age", 80)
# print(eight)
# hb = players_table.read("id", 174)
# print(hb)
# hb [2] +=1
# print(hb)
# players_table.write(hb)
# players_table.delete_row("id", 140)
schema = {"time": FLT}
# for id in range(1, 201):
#  s_taper.Taper(f"user{id}", "data.db").create_table(schema)
# for id in range(200):
#    idplayer = random.randint(1,200)
#    timenow = time.time()
#    pl_tab = s_taper.Taper(f"user{idplayer}", "data.db").create_table(schema)
#    pl_tab.write([timenow])
def count_players_online(total_players=200):
    online_count = 0
    for player_id in range(1, total_players + 1):
        pl_tab = s_taper.Taper(f"user{player_id}", "data.db").create_table(schema)
        times = pl_tab.read_all()
        if len(times) % 2 == 1:  
            online_count += 1
    print(f"Количество игроков онлайн: {online_count}")
count_players_online()

def alltime(id):
 pl_tab = s_taper.Taper(f"user{id}", "data.db").create_table(schema)
 ot = list(pl_tab.read_all())
 print(ot)
 for n, times in enumerate(ot):
    if n %2 == 0:
       start = times[0]
    else:
       end = times[0]
       print(end-start)
alltime(id = 2)

   
   

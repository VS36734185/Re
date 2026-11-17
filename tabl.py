import s_taper,random,faker
from s_taper.consts import *
fake = faker.Faker("ru_RU")
shema = {
    "id":INT+KEY,
    "name":TEXT,
     "intellegency":INT,
     "power":INT,
     "regeneration":FLT,
     "skill":INT,
}
tabl = s_taper.Taper("heroes","data.db").create_table(shema)

tabl.write([2,"Rogger",50,75,0.3,60])
for id in range (3,200):
    tabl.write([id,fake.user_name(),random.randint(0,100),random.randint(0,100),random.random(),random.randint(0,100)])
heroes = tabl.read_all()
print(heroes)
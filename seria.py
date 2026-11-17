import pickle, json,time,s_taper
from s_taper.consts import*
shema = {
    "id": INT+KEY,
    "invento": TEXT,
}

# Тестовый словарь инвентаря
inventory_test = {
    "sword": 1,
    "shield": 1,
    "potion": 5,
    "arrow": 20
}
tabl = s_taper.Taper("invento","data.db").create_table(shema)
tabl.write([1,inventory_test])

test = {}
for te in range(10):
    test[te] = f"{te*2}"
print(test)

re = pickle.dumps(test)
print(re)
vo = pickle.loads(re)
print(vo)

r = json.dumps(test)
print(r)
v = json.loads(r)
print(v)
test = {}
for te in range(2**20):
    test[te] = f"{te*2}"

start = time.time()
with open("data.pickle","wb") as file:
    pickle.dump(test,file)
print("pickle",time.time()-start)
start = time.time()
with open("data.json","w") as file:
  json.dump(test,file)
print("json",time.time()-start)
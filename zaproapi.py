import requests as req
url = "https://empty.free.beeceptor.com"
def reg(name,address):
    dan = {"name":name,"address":address}
    otv = req.post(url,data = dan)
    print(otv)
    print(otv.text)
reg("Sam","Adv,42")  
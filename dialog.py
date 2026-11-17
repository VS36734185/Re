import pyautogui as pyg

users = {"пользователь": "user"}
pyg.alert(title="Form site ", text="Hello", button="enter")
res = pyg.confirm(title="Form site", text="Are you have an account", buttons=["Yes", "No"])
print(res)
if res == "Yes":
    logi = pyg.prompt(title="Form site", text="write you login")
    passw = pyg.password(title="Form site", text="write you password")

    if logi in users and users[logi] == passw:
        pyg.alert(title="Вход", text="Успешный вход")
    else:
        pyg.alert(title="Вход", text="Неверный пароль")
else:
    logi = pyg.prompt(title="Вход", text="Введите логин")
    passq = pyg.password(title="Вход", text="Введите пароль")
    users[logi] = passq
    pyg.alert(title="Вход", text="Регистрация прошла успешно")
    print(users)
    feed = {}
    email = pyg.prompt(text = "Введите вашу почту", title = "Форма обратной связи")
    if email:
        review = pyg.prompt(text = "Введите ваш отзыв о сайте", title = "Форма обратной связи")
        if review:
            feed[email] = review
            pyg.alert(text = "Большое спасибо за отзыв", title = "Форма обратной связи")
        else:
            pyg.alert(text = "Отзыв не был введен", title = "Ошибка")
            
    else:
        pyg.alert(text = "Электронная почта не была введена",title = "Ошибка")
    
    print(feed)


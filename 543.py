book_phones = {
    'Сергей': '-79899899889',
    'Вячеслав': '112',
    'Неизвестный': '1',
    'Хирург ': '+09998765432',
    'Майк': '0'
}

    

def main():
    while True:
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        book_phones[name] = phone
        for key in book_phones:
            print(f"{key}: {book_phones[key]}")

if __name__ == "__main__":
    main()

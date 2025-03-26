library = {
    'война и мир': {
        "название": "война и мир",
        "год": "1868 1869",
        'автор': "Л.Н. Толстой",
        'страниц': '1472',
        'язык': 'русский'
    },
    'герой нашего времени': {
        "название": "герой нашего времени",
        "год": "1838 1839 1849",
        "автор": "М.Ю. Лермонтов",
        "страниц": "224",
        "язык": "русский"
    },
    "муму": {
        "название": "муму",
        "год": "1852",
        'автор': "И.С. Тургенев",
        "страниц": "120",
        "язык": "русский"
    }
}

while True:
    book = input("Выберите по чему вы будете искать:\n название, автор, год: ").strip().lower()
    
    if book == "название":
        name_book = input("Введите название: ").strip().lower()
        if name_book in library:
            book_info = library[name_book]
            print("Год: ", book_info["год"])
            print("Автор: ", book_info["автор"])
            print("Количество страниц: ", book_info["страниц"])
            print("Язык: ", book_info["язык"])
        else:
            print("В нашей библиотеке нет книги с названием", name_book)
    
    elif book == "год":
        year_to_find = input("Введите год, по которому вы хотите найти книги: ").strip()
        found_books = [book for book in library.values() if year_to_find in book["год"]]
        
        if found_books:
            for book in found_books:
                print("Название:", book["название"])
                print("Автор:", book["автор"])
                print("Количество страниц:", book["страниц"])
                print("Язык:", book["язык"])
        else:
            print("Книги за указанный год не найдены.")
            
    elif book == "автор":
        avtor_to_find = input("Введите автора, по которому вы хотите найти книгу: ").strip().lower()
        avtor_books = [book for book in library.values() if avtor_to_find in book["автор"].lower()]
        
        if avtor_books:
            for book in avtor_books:
                print("Название:", book["название"])
                print("Год:", book["год"])
                print("Количество страниц:", book["страниц"])
                print("Язык:", book["язык"])
        else:
            print("Книг данного автора у нас нет.")
    
    else:
        print("Некорректный ввод. Пожалуйста, выберите 'название', 'автор' или 'год'.")
    
    too = input("Вы хотите найти еще книгу? (да/нет): ").strip().lower()
    if too != "да":
        break

     
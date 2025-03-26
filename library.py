library = {
    'война и мир': {
        "название": "война и мир",
        "год": "1868" "1869",
        'автор': "Л.Н. Толстой",
        'страниц': '1472',
        'язык': 'русский'
    },
    'герой нашего времени': {
        "название": "герой нашего времени",
        "год": "1838" '1839' '1849',
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
book = input("выберете по чем вы будете искать:\n название, автор, год, ")
if book == "название":
    name_book = input("введите название ")
    if name_book in library:
        book_info = library[name_book]
        print("год: ", book_info["год"])
        print("автор: ", book_info["автор"])
        print("старниц: ", book_info["страниц"])
        print("язык: ", book_info["язык"])
    else :
        print("в нашей библиотеки нету книжки\n с названием", name_book)
else:
  if book == "год":
   year_to_find = input("Введите год, по которому вы хотите найти книги: ")

   found_books = [book for book in library.values() if book["год"].startswith(year_to_find) or year_to_find in book["год"]]

   if found_books:
      for book in found_books:
        print("Название:", book["название"])
        print("Автор:", book["автор"])
        print("Количество страниц:", book["страниц"])
        print("Язык:", book["язык"])

   else:
    print("Книги за указанный год не найдены.")
  else:
     if book == "автор":
         avtor_to_find = input("Введите автора по которому вы хотите найти книгу ")

         avtor_books = [book for book in library.values() if book["автор"].startswith(avtor_to_find) or avtor_to_find in book["автор"]]
         if avtor_books:
           for book in avtor_books:
            print("Название:", book["название"])
            print("год", book["год"])
            print("Количество страниц:", book["страниц"])
            print("Язык:", book["язык"])
         else:
            print("книг данного автора у нас нету")
        
  
     
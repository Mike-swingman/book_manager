## Это консольное приложение предназначено для управления библиотекой книг, хранящихся в JSON файле.


### Приложения включает в себя следующий функционал:

1. Добавить книгу: Добавление новой книги в библиотеку.
2. Удалить книгу: Удаление книги из библиотеки по ее ID.
3. Найти книгу: Поиск книг по автору, названию или году.
4. Показать все книги: Отображение списка всех книг в библиотеке.
5. Изменить статус книги: Изменение статуса книги (в наличии или выдана).
6. Выход: Выход из приложения.


## Запуск приложения:
1. Требования: Python 3.7+
2. Установка: Клонируйте репозиторий командой git clone
3. Запуск в терминале командой: python main.py


## Классы и методы

### Класс Book

Представляет книгу со следующими атрибутами:

* id: Уникальный идентификатор книги (генерируется автоматически).
* title: Название книги.
* author: Автор книги.
* year: Год издания.
* status: Статус книги (в наличии или выдана).

Методы:

* to_dict(): Преобразует экземпляр книги в словарь.
* __str__(): Возвращает строковое представление книги.



### Класс Library

Управляет коллекцией книг, хранящихся в JSON файле.

Методы:

* __init__(filename): Инициализирует библиотеку с указанным JSON файлом.
* load_books(): Загружает книги из JSON файла и преобразует их в экземпляры Book.
* dump_books(books): Сохраняет список экземпляров Book в JSON файл.
* add_book(): Запрашивает у пользователя данные книги и добавляет книгу в библиотеку.
* remove_book(): Запрашивает у пользователя ID книги и удаляет соответствующую книгу.
* find_book(): Запрашивает у пользователя параметры для поиска книги (автор, название или год).
* get_all_books(): Отображает все книги в библиотеке.
* change_book_status(): Запрашивает у пользователя ID книги и изменяет ее статус.

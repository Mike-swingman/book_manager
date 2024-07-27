import json
import os

from book import Book, BookStatus


class Library:
    def __init__(self, filename):
        self.filename = filename

    def load_books(self) -> list[Book]:
        """ Функция загружает книги из JSON файла и преобразует их в класс Book """

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            try:
                books = json.load(file)
                return [Book(**b) for b in books]
            except json.JSONDecodeError:
                return []

    def dump_books(self, books: list[Book]) -> None:
        """ Функция преобразует книги из класса Book в словарь и сохраняет в JSON файл"""

        with open(self.filename, 'w') as file:
            json.dump([b.to_dict() for b in books], file, indent=4)

    def add_book(self) -> None:
        """ Функция создает новую книгу """

        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год издания книги: ')

        if not year.isdigit():
            raise ValueError("Год издания книги должен быть числом")

        if not title or not author or not year:
            raise ValueError("Все поля должны быть заполнены.")

        # Проверяем наличие дубликата книги
        books = self.load_books()
        for existing_book in books:
            if existing_book.title == title and existing_book.author == author:
                raise ValueError(f"Книга с названием '{title}' у '{author}' уже есть.")

        # Создаем и сохраняем новую книгу
        book = Book(title, author, int(year))
        books.append(book)
        self.dump_books(books)
        print(f"Книга '{title}' '{author}' успешно добавлена.")

    def remove_book(self) -> None:
        """ Функция удаляет книгу по ID """

        book_id = input("Введите ID книги: ").strip()
        if not book_id:
            raise ValueError("Параметр ID не может быть пустым.")

        books = self.load_books()

        # Создаем новый список, исключая книгу с указанным ID
        updated_books = [book for book in books if book.id != book_id]

        # Сравниваем количество книг в обновленном списке с первоначальным списком books
        if len(updated_books) < len(books):
            self.dump_books(updated_books)
            print(f"Книга с ID '{book_id}' успешно удалена.")
        else:
            raise ValueError(f"Книга с ID '{book_id}' не найдена.")

    def find_book(self) -> None:
        """ Функция осуществляет поиск книги по параметру: автор, название, год """

        print('Введите цифру параметра по которому осуществляется поиск: 1. автор, 2. название, 3. год')
        search_by = input().strip()

        # Словарь для соответствия цифры параметру поиска
        search_dict = {
            '1': 'author',
            '2': 'title',
            '3': 'year'
        }

        if search_by not in search_dict:
            raise ValueError("Некорректный выбор параметра для поиска.")

        param_key = search_dict[search_by]  # Определяем параметр для поиска

        print(f'Введите {search_dict[search_by]}')
        param = input().strip()

        if not param:
            raise ValueError("Введены некорректные данные для поиска.")

        books = self.load_books()
        book_found = False  # Флаг, показывающий найдена ли книга

        for book in books:
            if getattr(book, param_key) == param:
                print(book)
                book_found = True

        if not book_found:
            raise ValueError(f'Книга не найдена.')

    def get_all_books(self) -> None:
        """ Функция отображает все книги, которые есть в библиотеке """

        books = self.load_books()

        if not books:
            print("В библиотеке нет книг.")

        for book in books:
            print(book)

    def change_book_status(self) -> None:
        """ Функция изменяет статус книги """

        book_id = input("Введите ID книги, которое хотите изменить: ").strip()

        if not book_id:
            raise ValueError("Параметр ID не может быть пустым.")

        books = self.load_books()
        book_found = False  # Флаг, показывающий найдена ли книга

        for book in books:
            if book.id == book_id:
                current_status = BookStatus(book.status)  # Получаем текущий статус книги
                new_status = BookStatus.booked if current_status == BookStatus.available else BookStatus.available
                print(f"Книга с ID: {book.id} найдена. Текущий статус: {current_status}.")
                choice = input(f"Вы хотите изменить статус на '{new_status}'? (да/нет): ").strip().lower()

                if choice == 'да':
                    book.status = new_status  # Присваиваем новый статус книги
                    self.dump_books(books)
                    print(f"Статус книги с ID '{book_id}' изменен на '{new_status}'.")
                    book_found = True
                else:
                    print("Статус книги не изменен.")
                break

        if not book_found:
            print(f"Книга с ID '{book_id}' не найдена.")

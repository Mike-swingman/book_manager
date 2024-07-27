import sys
from library import Library

library = Library('book_storage.json')


def print_menu() -> None:
    print("Библиотека книг:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать список всех книг")
    print("5. Изменить статус книги")
    print("6. Выход")


def exit_menu() -> None:
    print('Завершение работы с библиотекой')
    sys.exit()


menu_options = {
    '1': library.add_book,
    '2': library.remove_book,
    '3': library.find_book,
    '4': library.get_all_books,
    '5': library.change_book_status,
    '6': exit_menu
}


def main() -> None:
    while True:
        print_menu()
        choice = input("Выберите необходимый пункт: ")
        try:
            menu_options[choice]()
        except KeyError:
            print("Такого пункта нет в меню. Попробуйте ещё раз")
        except ValueError as e:
            print('Ошибка:', e)


if __name__ == "__main__":
    main()

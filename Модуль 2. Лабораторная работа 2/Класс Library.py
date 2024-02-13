BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        :return: Строка с названием книги
        """
        return 'Книга "{}"'.format(self.name)

    def __repr__(self) -> str:
        """
        :return: Строка с параметрами книги
        """
        return 'Book(id_={}, name={!r}, pages={})'.format(self.id, self.name, self.pages)


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None):
        """
        :param books: Список книг (необязательный аргумент)
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        :return: Следующий идентификатор
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        :param book_id: Идентификатор книги
        :raise ValueError: Если книги с таким идентификатором нет, то вызывается ошибка
        :return: Индекс книги в списке
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

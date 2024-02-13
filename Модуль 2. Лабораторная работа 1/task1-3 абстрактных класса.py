import doctest

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Л.Н. Толстой", 1225) # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def read_book(self, page: int) -> None:
        """
        Чтение книги с определенной страницы.

        :param page: Страница, с которой начинается чтение
        :raise ValueError: Если страница не входит в диапазон от 1 до pages, то вызывается ошибка

        Примеры:
        >>> book = Book("Война и мир", "Л.Н. Толстой", 1225)
        >>> book.read_book(100)
        """
        if not isinstance(page, int):
            raise TypeError("Страница должна быть типа int")
        if page < 1 or page > self.pages:
            raise ValueError("Страница должна быть в диапазоне от 1 до {}".format(self.pages))
        ...

    def get_info(self) -> str:
        """
        Получение информации о книге.

        :return: Строка с названием, автором и количеством страниц книги

        Примеры:
        >>> book = Book("Война и мир", "Л.Н. Толстой", 1225)
        >>> book.get_info()
        'Книга "Война и мир" автора Л.Н. Толстой, 1225 страниц'
        """
        return 'Книга "{}" автора {}, {} страниц'.format(self.title, self.author, self.pages)


class Flower:
    def __init__(self, name: str, color: str, petals: int):
        """
        Создание и подготовка к работе объекта "Цветок"

        :param name: Название цветка
        :param color: Цвет цветка
        :param petals: Количество лепестков у цветка

        Примеры:
        >>> flower = Flower("Роза", "Красный", 5) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название цветка должно быть типа str")
        if not name:
            raise ValueError("Название цветка не может быть пустым")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Цвет цветка должен быть типа str")
        if not color:
            raise ValueError("Цвет цветка не может быть пустым")
        self.color = color

        if not isinstance(petals, int):
            raise TypeError("Количество лепестков должно быть типа int")
        if petals <= 0:
            raise ValueError("Количество лепестков должно быть положительным числом")
        self.petals = petals

    def smell_flower(self) -> None:
        """
        Запах цветка.

        Примеры:
        >>> flower = Flower("Роза", "Красный", 5)
        >>> flower.smell_flower()
        """
        ...

    def water_flower(self, amount: float) -> None:
        """
        Полив цветка.

        :param amount: Количество воды в литрах
        :raise ValueError: Если количество воды отрицательное или равное нулю, то вызывается ошибка

        Примеры:
        >>> flower = Flower("Роза", "Красный", 5)
        >>> flower.water_flower(0.5)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество воды должно быть типа int или float")
        if amount <= 0:
            raise ValueError("Количество воды должно быть положительным числом")
        ...

    def change_color(self, new_color: str) -> None:
        """

        Смена цвета цветка.

        :param new_color: Новый цвет цветка
        :raise ValueError: Если новый цвет совпадает со старым, то вызывается ошибка

        Примеры:
        >>> flower = Flower("Роза", "Красный", 5)
        >>> flower.change_color("Белый")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")
        if not new_color:
            raise ValueError("Новый цвет не может быть пустым")
        if new_color == self.color:
            raise ValueError("Новый цвет не может совпадать со старым")
        self.color = new_color


class Pot:
    def __init__(self, material: str, volume: float, weight: float):
        """
        Создание и подготовка к работе объекта "Кастрюля"

        :param material: Материал кастрюли
        :param volume: Объем кастрюли в литрах
        :param weight: Вес кастрюли в килограммах

        Примеры:
        >>> pot = Pot("Алюминий", 3, 0.5) # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал кастрюли должен быть типа str")
        if not material:
            raise ValueError("Материал кастрюли не может быть пустым")
        self.material = material

        if not isinstance(volume, (int, float)):
            raise TypeError("Объем кастрюли должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем кастрюли должен быть положительным числом")
        self.volume = volume

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кастрюли должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес кастрюли должен быть положительным числом")
        self.weight = weight

    def cook_soup(self, ingredients: list) -> None:
        """
        Готовка супа в кастрюле.

        :param ingredients: Список ингредиентов для супа
        :raise ValueError: Если список ингредиентов пустой, то вызывается ошибка

        Примеры:
        >>> pot = Pot("Алюминий", 3, 0.5)
        >>> pot.cook_soup(["Картошка", "Морковь", "Лук", "Вода", "Соль"])
        """
        if not isinstance(ingredients, list):
            raise TypeError("Ингредиенты должны быть типа list")
        if not ingredients:
            raise ValueError("Ингредиенты не могут быть пустыми")
        ...

    def wash_pot(self) -> None:
        """
        Мытье кастрюли.

        Примеры:
        >>> pot = Pot("Алюминий", 3, 0.5)
        >>> pot.wash_pot()
        """
        ...

    def break_pot(self) -> None:
        """
        Сломать кастрюлю.

        Примеры:
        >>> pot = Pot("Алюминий", 3, 0.5)
        >>> pot.break_pot()
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
# Животные — базовый класс. Дикие и домашние животные— дочерние классы.

# Базовый класс Животное
class Animal:
    # Конструктор init, принимающий атрибуты имя, вид и вес
    def __init__(self, name: str, species: str, weight: float) -> None:
        self.name = name
        self.species = species
        self.weight = weight

    def __str__(self) -> str:
        # Форматирование строки с атрибутами
        return f"{self.name} is a {self.species} and weighs {self.weight} kg"

    # Магический метод repr, возвращающий строку, которая может быть использована для создания объекта
    def __repr__(self) -> str:
        # Форматирование строки с именем класса и атрибутами
        return f"Animal({self.name!r}, {self.species!r}, {self.weight!r})"

    # Метод feed, который кормит животное
    def feed(self, food: str) -> None:
        # Вывод сообщения о кормлении животного
        print(f"{self.name} is eating {food}.")

    # Метод sleep, который усыпляет животное
    def sleep(self) -> None:
        # Вывод сообщения об усыплении животного
        print(f"{self.name} is sleeping.")


# Дочерний класс Дикие животные, наследующий от базового класса Животное
class WildAnimal(Animal):
    # Конструктор init, расширяющий конструктор базового класса атрибутом опасность
    def __init__(self, name: str, species: str, weight: float, danger: str) -> None:
        # Вызов конструктора базового класса
        super().__init__(name, species, weight)
        # Инициализация атрибута опасности
        self.danger = danger

    # Магический метод str, перегружающий метод базового класса
    def __str__(self) -> str:
        # Форматирование строки с атрибутами, включая опасность
        return f"{self.name} is a {self.species} and weighs {self.weight} kg. It is {self.danger}."

    # Магический метод repr, перегружающий метод базового класса
    def __repr__(self) -> str:
        # Форматирование строки с именем класса и атрибутами, включая опасность
        return f"WildAnimal({self.name!r}, {self.species!r}, {self.weight!r}, {self.danger!r})"

    # Метод hunt, который охотится на добычу
    def hunt(self, prey: str) -> None:
        # Вывод сообщения об охоте на добычу
        print(f"{self.name} is hunting {prey}.")

    # Метод sleep, перегружающий метод базового класса
    def sleep(self) -> None:
        # Вывод сообщения об усыплении животного с уточнением места
        print(f"{self.name} is sleeping in the wild.")
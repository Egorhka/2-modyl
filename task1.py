from abc import ABC, abstractmethod

# Класс для описания Стола
class Table(ABC):
    def __init__(self, material: str, height: float, length: float, width: float):
        """
        Инициализация стола.

        :param material: Материал стола (например, дерево, металл).
        :param height: Высота стола в сантиметрах.
        :param length: Длина стола в сантиметрах.
        :param width: Ширина стола в сантиметрах.
        """
        self.material = material
        self.height = height
        self.length = length
        self.width = width
        self._validate()

    def _validate(self):
        """Проверка значений атрибутов."""
        if self.height <= 0 or self.length <= 0 or self.width <= 0:
            raise ValueError("Размеры стола должны быть больше нуля.")

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Метод для вычисления площади стола.

        :return: Площадь стола в квадратных сантиметрах.
        :rtype: float
        """
        ...

    @abstractmethod
    def change_material(self, new_material: str) -> None:
        """
        Метод для изменения материала стола.

        :param new_material: Новый материал для стола.
        :return: None
        """
        ...


# Класс для описания Дерева
class Tree(ABC):
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева.

        :param species: Вид дерева (например, дуб, сосна).
        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.
        """
        self.species = species
        self.height = height
        self.age = age
        self._validate()

    def _validate(self):
        """Проверка значений атрибутов."""
        if self.height <= 0 or self.age <= 0:
            raise ValueError("Высота и возраст дерева должны быть больше нуля.")

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Метод для роста дерева на определённое количество лет.

        :param years: Количество лет, на которое вырастет дерево.
        :return: None
        """
        ...

    @abstractmethod
    def drop_leaves(self) -> None:
        """
        Метод для опадания листьев.

        :return: None
        """
        ...


# Класс для описания Пользователя в социальной сети
class SocialMediaUser(ABC):
    def __init__(self, username: str, age: int, email: str):
        """
        Инициализация пользователя.

        :param username: Имя пользователя.
        :param age: Возраст пользователя.
        :param email: Электронная почта пользователя.
        """
        self.username = username
        self.age = age
        self.email = email
        self._validate()

    def _validate(self):
        """Проверка значений атрибутов."""
        if self.age < 13:
            raise ValueError("Возраст пользователя должен быть не меньше 13 лет.")
        if "@" not in self.email:
            raise ValueError("Некорректный формат электронной почты.")

    @abstractmethod
    def post_content(self, content: str) -> None:
        """
        Метод для размещения контента.

        :param content: Контент для размещения.
        :return: None
        """
        ...

    @abstractmethod
    def update_profile(self, new_username: str) -> None:
        """
        Метод для обновления имени пользователя.

        :param new_username: Новое имя пользователя.
        :return: None
        """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        """возвращает список RGB цветов"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """проверяет корректность переданных значений перед установкой нового цвета."""
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255) and (
                isinstance(r, int) and isinstance(r, int) and isinstance(r, int)):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        """возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
         False - во всех остальных случаях."""
        pass

    def get_sides(self):
        return self.__sides

    def __len__(self):
        """должен возвращать периметр фигуры"""
        pass

    def set_sides(self, *new_sides):
        """должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
         в противном случае - менять."""
        # if len(new_sides) == self.sides_count:

        pass

    pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        """рассчитать исходя из длины окружности (одной единственной стороны)."""
        if len(sides) != self.sides_count:
            sides = (1 for _ in range(self.sides_count))
        Figure.__init__(self, color, sides)
        self.__radius = 0

    def get_square(self):  # возвращает площадь круга
        pass

    pass


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
        Figure.__init__(self, color, sides)
    def get_square(self):  # возвращает площадь треугольника
        pass

    pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        """Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)"""
        if len(sides) == 1 and len(sides) != self.sides_count:
            sides = [sides[0] for _ in range(self.sides_count)]
        Figure.__init__(self, color, sides)

    def get_volume(self):  # возвращает объём куба
        pass

    pass


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

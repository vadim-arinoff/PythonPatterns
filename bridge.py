from abc import ABC, abstractmethod

#абстрактный класс Shape, конкретные реализации Circle и Square, класс Color. круг и квадрат используют разные цвета для отрисовки.
# Абстрактный класс "Фигура"
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# Конкретная реализация "Круг"
class Circle(Shape):
    def draw(self):
        return f"Drawing a circle in {self.color}."

# Конкретная реализация "Квадрат"
class Square(Shape):
    def draw(self):
        return f"Drawing a square in {self.color}."

# Конкретная реализация "Цвет"
class Color:
    def __init__(self, name):
        self.name = name

# Создание объектов фигур с разными цветами
red_color = Color("red")
green_color = Color("green")

red_circle = Circle(red_color)
green_square = Square(green_color)

# Вывод результатов
print(red_circle.draw())
print(green_square.draw())
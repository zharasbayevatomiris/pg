import math

class Shape:
    def __init__(self, shape_name=None):
        self.shape_name = shape_name
    
    def __str__(self):
        return f'{self.shape_name} shape with area {self.area()}'

    def area(self):
        # Obecná třída Shape nemá implementovanou metodu area, proto vrací 0.0
        return 0.0


class Rectangle(Shape):
    def __init__(self, width, height):
        # Voláme konstruktor nadřazené třídy a nastavíme název tvaru
        super().__init__('Rectangle')
        self.width = width
        self.height = height
    
    def area(self):
        # Plocha obdélníku je šířka * výška
        return round(self.width * self.height, 1)


class Circle(Shape):
    def __init__(self, radius):
        # Voláme konstruktor nadřazené třídy a nastavíme název tvaru
        super().__init__('Circle')
        self.radius = radius
    
    def area(self):
        # Plocha kruhu je π * r^2
        return round(math.pi * (self.radius ** 2), 1)
    
    def __str__(self):
        # Vlastní __str__ pro kruh
        return f"{self.shape_name} with a radius of {self.radius} has an area of {self.area()}"


# Unit testy
def test_shapes():
    # Test pro obdélník
    rect = Rectangle(4, 5)
    assert rect.area() == 20.0
    assert str(rect) == "Rectangle shape with area 20.0"

    # Test pro kruh
    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
    assert str(circle) == "Circle shape with a radius of 3 has an area of 28.3"


if __name__ == "__main__":
    # Ukázka použití tříd
    shape = Shape()
    print(shape)  # Vytiskne "None shape with area 0.0"
    rect = Rectangle(4, 5)
    print(rect)  # Vytiskne "Rectangle shape with area 20.0"
    circle = Circle(3)
    print(circle)  # Vytiskne "Circle with a radius of 3 has an area of 28.3"

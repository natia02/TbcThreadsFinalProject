from Trapezoid import Trapezoid


class Rectangle(Trapezoid):
    def __init__(self, parameters=None):
        super().__init__((parameters[0], 0, parameters[1]))

    def area(self):
        return self.height * self.base1

    def __str__(self):
        return f"Rectangle with width = {self.base1} and height = {self.height}"


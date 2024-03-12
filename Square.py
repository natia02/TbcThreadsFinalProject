from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, parameters=None):
        super().__init__((parameters[0], 0, 0))

    def __str__(self):
        return f"Square with side length {self.base1}"

    def area(self):
        return pow(self.base1, 2)


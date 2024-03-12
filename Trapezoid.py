class Trapezoid:
    # parameters is the list of [base1, base2, height]
    def __init__(self, parameters=None):
        if parameters is None:
            self.base1 = 0
            self.base2 = 0
            self.height = 0
        self.base1 = parameters[0]
        self.base2 = parameters[1]
        self.height = parameters[2]

    def __str__(self):
        return f"trapezoid with base1 = {self.base1}, base2 = {self.base2}, height = {self.height}"

    def area(self):
        return (self.base1 + self.base2) / 2 * self.height

    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()
        return False

    def __le__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() <= other.area()
        return False

    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()

        return False

    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)
        return False

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() + other.area()
        return -1

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() - other.area()
        return -1

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() % other.area()
        return -1

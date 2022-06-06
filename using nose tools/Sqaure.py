class Square:
    def __init__(self, side):
        self.side = side
        if not isinstance(self.side, (int, float)):
            raise TypeError('side must be an integer')
        elif not 100 >= self.side >= 0:
            raise ValueError("side must be between 0 and 100")

    def area(self):
        return round(self.side * self.side, 2)
    def perimeter(self):
        return round(4 * self.side, 2)

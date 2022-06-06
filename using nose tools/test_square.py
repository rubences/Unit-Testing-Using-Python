from Square import Square
from nose.tools import *

class TestingSquareCreation:
    #Check behaviour of init function.
    def test_creating_square_with_numeric_side(self):
        object = Square(25)
        object2 = Square(25.0)
    def test_creating_square_with_negative_side(self):
        with assert_raises(ValueError):
            object = Square(-25)
            object2 = Square(-25.0)
    def test_creating_square_with_greaterthan_side(self):
        with assert_raises(ValueError):
            object = Square(110)
    def test_creating_square_with_nonnumeric_side(self):
        with assert_raises(TypeError):
            object = Square('side')
    
    #Computing area.
    def test_squarearea_with_random_numeric_side(self):
        object = Square(20)
        print(object.area())
    def test_squarearea_with_min_side(self):
        object = Square(0)
        print(object.area())
    def test_squarearea_with_max_side(self):
        object = Square(100)
        print(object.area())

    # Computing perimeter.
    def test_squareperimeter_with_random_numeric_side(self):
        object = Square(20)
        print(object.perimeter())

    def test_squareperimeter_with_min_side(self):
        object = Square(0)
        print(object.perimeter())

    def test_squareperimeter_with_max_side(self):
        object = Square(100)
        print(object.perimeter())

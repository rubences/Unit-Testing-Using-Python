# Unit-Testing using nose tools

### Tasks
Define a class 'Square' with the following specifications (Square.py):
* Define a class method '__init__', which initializes the instance of 'Square' and accepts an input through arguement 'side'.
* Input side must be an integer or float type. If not, then it must raise a TypeError with 'side must be an integer or float' message.
* Input side must be between 0 and 100. If not, then it must raise a ValueError with 'side must be between 0 and 100' message.
* Define a class method 'area', which compute the area of a square rounded upto 2 decimal values.
* Define a class method 'perimeter', which compute the perimeter of a square rounded upto 2 decimal values.

#### Test-Cases
Define a nose test class 'TestingSquareCreation' with the following specifications (test_square.py):
##### Check the behavior of init method
* Define a class method 'test_creating_square_with_numeric_side' which creates a square with a numeric integer or float.
* Define a class method 'test_creating_square_with_negative_side' and check if it throws ValueError with 'side must be between 0 and 100' message.
* Define a class method 'test_creating_square_with_greaterthan_side' and check if it throws ValueError with 'side must be between 0 and 100' message.
* Define a class method 'test_creating_square_with_nonnumeric_side' and check if it throws TypeError with 'side must be an integer or float' message.

##### Check behavior of area method
* Define a class method 'test_squarearea_with_random_numeric_side' which computes the square area with any random numeric integer or float.
* Define a class method 'test_squarearea_with_min_side' which computes the square area with the minimum numeric integer or float.
* Define a class method 'test_squarearea_with_max_side' which computes the square area with the maximum numeric integer or float.

##### Check behavior of perimeter method
* Define a class method 'test_squareperimeter_with_random_numeric_side' which computes the square perimeter with any random numeric integer or float.
* Define a class method 'test_squareperimeter_with_min_side' which computes the square perimeter with the minimum numeric integer or float.
* Define a class method 'test_squareperimeter_with_max_side' which computes the square perimeter with the maximum numeric integer or float.

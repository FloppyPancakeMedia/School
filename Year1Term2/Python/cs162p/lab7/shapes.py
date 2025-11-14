from abc import ABC, abstractmethod

class Point(ABC):

    def set_symbol(self, symbol):
        self._symbol = symbol
    
    @abstractmethod
    def draw(self):
        pass

    def __str__(self):
        return self._name


class Triangle(Point):
    def __init__(self, size, symbol = '#'):
        self._symbol = symbol
        self._size = size
        self._name = "Triangle"

    
    def draw(self):
        x = 1
        while x < self._size:
            for i in range(x):
                print(self._symbol, end='')
            x += 1
            print('')


class Diamond(Point):
    def __init__(self, size = 3,symbol = '#'):
        self._symbol = symbol
        self._size = size
        self._name = "Diamond"

        # Limit diamond to min size of 3
        if self._size < 3:
            print("Invalid size. Resetting to 3.")
            self._size = 3

    def draw(self):
        # Top part of diamond
        for i in range(1, self._size + 1):
            for j in range(1, self._size - i + 1):
                 print(" ", end = "")
            for j in range(1, 2 * i):
                print(self._symbol, end = "")
            print()

        # Lower part of diamond
        for i in range(self._size - 1, 0, -1):
            for j in range(1, self._size - i + 1):
                print(" ", end = "")
            for j in range(1, 2 * i):
                print(self._symbol, end = "")
            print()

class Rectangle(Point):
    def __init__(self, height, width, symbol = '#'):
        self._symbol = symbol
        self._height = height
        self._width = width
        self._name = "Rectangle"
    
    def draw(self):
        for x in range(self._height):
            for y in range(self._width):
                print(self._symbol, end = '')
            print()

class Square(Rectangle):
    def __init__(self, size, symbol = '#'):
        super().__init__(size, size, symbol)
        self._name = "Square"

class Rhombus(Rectangle):
    def __init__(self, height, width, symbol = '#'):
        super().__init__(height, width, symbol)
        self._name = "Rhombus"

    def draw(self):
        for x in range(self._height):
            # Add space each new line
            for i in range(x): print(" ", end='')
            for y in range(self._width):
                print(self._symbol, end='')
            print()

class Hexagon(Point):
    def __init__(self, size, symbol='#'):
        self._size = size
        self._symbol = symbol
        self._name = "Hexagon"
    
    def draw(self):
        # Top part
        for i in range(self._size - 1):
            for j in range(self._size - 1 - i):
                print(" ", end='')
            for j in range(self._size + (i * 2)):
                print(self._symbol, end="")
            print()
        
        # Middle
        for i in range(self._size):
            for j in range(self._size + (2 * (self._size - 1))):
                print(self._symbol, end = "")
            print()
        
        # Bottom
        for i in range(self._size - 2, -1, -1):
            for j in range(self._size - 1 - i):
                print(" ", end="")
            for j in range(self._size + (i * 2)):
                print(self._symbol, end="")
            print()

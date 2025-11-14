class Point:
    def __init__(self, symbol = '#'):
        self._symbol = symbol
        self._name = "Point"
    
    def set_symbol(self, symbol):
        self._symbol = symbol
        
    def draw(self):
        print(self._symbol)

    def __str__(self):
        return self._name


class Triangle(Point):
    def __init__(self, size, symbol = '#'):
        super().__init__(symbol)
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
    def __init__(self, symbol = '#', size = 3):
        super().__init__(symbol)
        self._size = size
        self._name = "Diamond"

        # Limit diamond to odd numbers and min size of 3
        if size % 2 != 1:
            print("Invalid diamond size. Converting to odd number")
            self._size -= 1
        if self._size < 3:
            print("Invalid size. Resetting to 3.")
            self._size = 3
    

    def draw(self):
        # Top part of diamond
        for i in range(1, self._size + 1):
            for j in range(1, self._size - i + 1):
                 print(" ", end = "")
            for j in range(1 , 2 * i):
                print(self._symbol, end = "")
            print()

        # Lower part of diamond
        for i in range(self._size - 1, 0, -1):
            for j in range(1,self._size - i + 1):
                print(" ", end = "")
            for j in range(1, 2 * i):
                print(self._symbol, end = "")
            print()

class Rectangle(Point):
    def __init__(self, height, width, symbol = '#'):
        super().__init__(symbol)
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
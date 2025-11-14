from shapes import *
import sys

filename = sys.argv[1]
shapes : list = []

try:
    file = open(filename, "r")

    while(True):
        line = file.readline()
        data = line.split(" ")
        if not line: break

        shape = None
        match data[0]:
            case 'P':
                symbol = data[1]
                shape = Point(symbol)
            case 'S':
                symbol = data[1]
                size = int(data[2])
                shape = Square(size, symbol)
            case 'T':
                symbol = data[1]
                size = int(data[2])
                shape = Triangle(size, symbol)
            case 'D':
                symbol = data[1]
                size = int(data[2])
                shape = Diamond(symbol, size)
            case 'R':
                symbol = data[1]
                height = int(data[2])
                width = int(data[3])
                shape = Rectangle(height, width, symbol)
        
        shapes.append(shape)

    for s in shapes:
        print(f"Now presenting... SHAPE: {s}!!!")
        s.draw()
        print()


except Exception as e:
    print(f"An exception has occured: {e}")

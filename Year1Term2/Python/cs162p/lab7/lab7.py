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
            case 'H':
                symbol = data[1]
                height = int(data[2])
                width = int(data[3])
                shape = Rhombus(height, width, symbol)
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
                shape = Diamond(size, symbol)
            case 'R':
                symbol = data[1]
                height = int(data[2])
                width = int(data[3])
                shape = Rectangle(height, width, symbol)
            case 'X':
                symbol = data[1]
                size = int(data[2])
                shape = Hexagon(size, symbol)
        
        shapes.append(shape)

    for s in shapes:
        print(f"Now presenting... SHAPE: {s}!!!")
        s.draw()
        print()


except Exception as e:
    print(f"An exception has occured: {e}")

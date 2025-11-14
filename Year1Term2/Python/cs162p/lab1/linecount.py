import sys
import os

filename = sys.argv[1]

try:
    file = open(filename, 'r')

    num_lines = 0

    while (True):
        line = file.readline()
        if not line: break
        num_lines += 1

    file.close()

    print("Lines found: %d" % num_lines)
except:
    print("error reading file")

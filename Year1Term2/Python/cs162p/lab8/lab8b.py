import sys, pascal

depth = int(sys.argv[1])

t = pascal.Pascal(depth)

t.populate_data()
t.draw()
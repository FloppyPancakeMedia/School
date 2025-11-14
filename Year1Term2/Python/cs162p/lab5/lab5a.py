from reversemath import ReverseFloat
import sys

x = sys.argv[1]
y = sys.argv[2]


reverse_x : ReverseFloat = ReverseFloat(float(x))
reverse_y : ReverseFloat = ReverseFloat(float(y))

print(str(reverse_x))
print("x + y = %s" % str(reverse_x + reverse_y))
print("x - y = %s" % str(reverse_x - reverse_y))
print("x * y = %s" % str(reverse_x * reverse_y))
print("x / y = %s" % str(reverse_x / reverse_y))
from mathstuff import MyMath

a : int = 5
b : int = -68
mm = MyMath()

print(mm.absolute(a))
print(mm.absolute(b))

nums : list[float] = [1, 2.2, 3.5, 5, 4, 4.4, 1203.78746]

print(mm.average(nums))
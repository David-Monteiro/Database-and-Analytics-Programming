###NumPy Exercise 1

b = numpy.arange(24).reshape(2,3,4)
row1 = numpy.array([0, 0, 0])
column1 = numpy.array([0, 1, 2])
print(numpy.arange(24))
print("\n")
print(b)
print("\n")
print(b[row1, column1])
print("\n")
row2 = numpy.array([1, 2, 3])
column2 = numpy.array([0, 1, 2])
print(b[row2, column2])
import numpy


foo = numpy.array(input().strip().split(), float)
bar = numpy.array(input().strip().split(), int)

foo = list(foo)
print(numpy.polyval(foo, bar[0]))


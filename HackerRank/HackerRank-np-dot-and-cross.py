import numpy

dim = tuple(map(int, input().split()))
dim = dim[0]

foo = [input().strip().split() for _ in range(dim)]
bar = [input().strip().split() for _ in range(dim)]
foo = numpy.array(foo, int)
bar = numpy.array(bar, int)

print(foo @ bar)





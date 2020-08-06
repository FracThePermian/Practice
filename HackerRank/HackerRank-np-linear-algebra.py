import numpy

dim = tuple(map(int, input().split()))
foo = [input().strip().split() for _ in range(dim[0])]
foo = numpy.array(foo, float)

print(numpy.linalg.det(foo))



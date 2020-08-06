import numpy

n, m = map(int, input().split())

foo = [input().strip().split() for _ in range(n)]
matrix = numpy.array(foo, int)

matrix = numpy.min(matrix, axis=1)
print(numpy.max(matrix))









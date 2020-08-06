import numpy

n, m = map(int, input().split())

foo = [input().strip().split() for _ in range(n)]

matrix = numpy.array(foo, int)

matrix = numpy.sum(matrix, axis= 0)
print(numpy.prod(matrix, axis= None))

import numpy

n, m = map(int, input().split())
foo = [input().strip().split() for _ in range(n)]
matrix = numpy.array(foo, int)


print(numpy.mean(matrix, axis=1), numpy.var(matrix, axis=0), numpy.std(matrix, axis=None), sep='\n')


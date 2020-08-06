import numpy

n, m = map(int, input().split())

foo = [input().strip().split() for _ in range(n)]
foo = numpy.array(foo, int)

print(foo.transpose())
print(foo.flatten())

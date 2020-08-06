import numpy

n, m = map(int, input().split())

if n == m:
    print(numpy.identity(n))
else:
    print(numpy.eye(n,m))



import numpy

n, m = map(int, input().split())

foo = numpy.zeros((n,m), int)
bar = numpy.zeros((n,m), int)
for i in range(n):
    foo[i] = numpy.array(input().split(), int)
for i in range(n):
    bar[i] = numpy.array(input().split(), int)

print(foo + bar, foo - bar, foo * bar, foo // bar, foo % bar, foo ** bar, sep='\n')



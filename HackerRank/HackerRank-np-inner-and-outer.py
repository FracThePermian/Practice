import numpy

foo = input().strip().split()
bar = input().strip().split()
foo = numpy.array(foo, int)
bar = numpy.array(bar, int)


print(numpy.inner(foo, bar), numpy.outer(foo, bar), sep='\n')










import numpy

a = input().strip().split()


a = numpy.array(a, float)

print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep='\n')


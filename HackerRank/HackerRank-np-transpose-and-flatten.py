import numpy

n, m = map(int, input().split())

x = 1
ij1 = []
ij2 = []

while True:
    foo, bar = map(int, input().split())
    ij1.append(foo)
    ij2.append(bar)
    if x <n:
        x += 1
    else:
        break

ij1 = numpy.array([ij1])
ij2 = numpy.array([ij2])
matrix = numpy.concatenate((ij1, ij2), axis=0)
matrix = matrix.T
print(matrix.transpose())
print(matrix.flatten())




# array = numpy.array([input().strip().split() for _ in range(n)], int)
#
# print(array, type(array), 'hello')


# array = numpy.array([input().strip().split() for _ in range(n)], int)
# print (array.transpose())
# print (array.flatten())














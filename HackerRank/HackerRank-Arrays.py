import numpy


def arrays(arr):
    print('enter loop')
    arr = numpy.array((arr), float)
    print(arr)
    arr = arr[::-1]
    print(arr)
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)





# 1 2 3 4 -8 -10


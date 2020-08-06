import numpy

n, m, p = map(int, input().split())

foo = [input().strip().split() for _ in range(n)]

bar = [input().strip().split() for _ in range(m)]


n_matrix = numpy.array(foo, int)
m_matrix = numpy.array(bar, int)

b = n + m
main_matrix = numpy.concatenate((n_matrix, m_matrix)).reshape(b,p)
print(main_matrix)



# matrix = numpy.concatenate((n_matrix, m_matrix), int)




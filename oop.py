import numpy as np
import scipy



#Object Orientated Programming in Python

x = 1
print(type('hello')) #'hello' is an object of the class str
print(type(x))      # x is an object of class int

def hello():
    print('hello')

print(type(hello)) #hello is an object of the class 'function'

x = 1
y = 'hello'

# print(x+y) Unsupported operand type for +: 'int' and 'str'

string = 'hello'
print(string.upper()) #upper is a method
print(type(string.upper()))



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def identify(self):
        print(self.name, self.age)

    def get_age(self):
        return self.age





boy = Dog('good', 'boy')
boy.identify()
boy.get_age()
print(boy.get_age())

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print('CLASS IS FULL')


physics = Course('Physics', 3)
physics.add_student('Sam Petzold')
physics.add_student('Wee Wee')
physics.add_student('foo foo')
physics.add_student('cha cha')




print('hello world')

print('i love it. (upper)'.upper())
print('i love it. (rjust)'.rjust(20))
print('i love it. '.upper().rjust(20))
print('i love it'.capitalize())
print('               I love it        (strip'.strip())

print(f'{print} (print a function)')
print(f'{type(229)} (print a type)')


np.array([1,2])
array_1d = np.array([1,2,3,4])
print(array_1d, type(array_1d))


array_1d = np.array([1,2,3,4])
array_4by1 = np.array([[1,2,3,4]])
large_array = np.array([i for i in range(400)])
large_array = large_array.reshape((20,20))
from_list = np.array([1,2,3])
from_list_2d = np.array([[1,2,3.0], [4,5,6]])
from_list_bad_type = np.array([1,2,3,'a'])
print(f'Data type of integer is {from_list.dtype}')
print(f'Data type of float is {from_list_2d.dtype}')

print(array_1d,array_4by1,large_array,from_list_2d,from_list_bad_type)
print(type(from_list_bad_type))
print('\n\n', array_1d + 5)
print('\n\n', array_1d*5)
print(np.sqrt(array_1d), np.power(array_1d,2), np.exp(array_1d), np.log(array_1d))
array_1d @ array_1d
print(array_1d @ array_1d)
array_1d.dot(array_1d)
print(array_1d.dot(array_1d), np.dot(array_1d, array_1d))

weight_matrix = np.array([1,2,3,4]).reshape(2,2)
sample = np.array([[50,60]]).T
np.matmul(weight_matrix, sample)
print(weight_matrix)
print(sample)
print(np.matmul(weight_matrix, sample))
mat1 = np.array([[1,2], [3,4]])
mat2 = np.array([[5,6], [7,9]])
print(np.matmul(mat1,mat2))
a = np.array([i for i in range(10)])
print(a, a*a, np.multiply(a,10) )

samples = np.random.random((15,5))
print('\n\n', samples)
expanded1 = np.expand_dims(samples, axis=1)
tile1 = np.tile(expanded1, (1, samples.shape[0], 1))
print(tile1)
expanded2 = np.expand_dims(samples, axis=0)
tile2 = np.tile(expanded2, (samples.shape[0], 1, 1))
print(expanded2, tile2)
diff = tile2 - tile1
print(diff)
distances = np.linalg.norm(diff, axis=1)
print(distances)
diff = samples[: , np.newaxis, :] - samples[np.newaxis, :, :]
print(diff)
distances = np.linalg.norm(diff, axis=-1)
print(distances)
# print(distances = np.linalg.norm(diff, axis=-1))
# print(distances = scipy.spatial.distance.cdist(samples, samples))


#vectorizing your code makes it run much faster
a = np.random.random(50000)
b = np.random.random(50000)

dot = 0.0
for i in range(len(a)):
    dot += a[i] * b[i]
print(dot)
print(np.array(a).dot(np.array(b)))






















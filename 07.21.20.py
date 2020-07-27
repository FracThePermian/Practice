#import myfile
import random
import math
import json
import csv
import struct


# print(dir(myfile))
#
# dir(myfile)

# Number object-type
x = [123.123, 3.1415, 0b111];
y = 123.778;
print(x);

z = y;

# Strings object-type
spam = 'spam';
name = "Bob's";
blob = b'a/x01c';
up = u'sp/xc4m';
print(up, blob)
print(b'a/x01c', u'sp/xc3m', 'comment')

# List object-type
print([1, [2, 'three'], 4.5], list(range(10)))

# Dictionary object-type
# Tuples object-type
print((1, 'spam', 4, 'U'))
print(tuple('spam'))

# file object-type
#
# open('eggs.txt'), open(r'C:\ham.bin', 'wb')

# Sets
print(set('abc'))
print({'a', 'ab', 'c'})

# boolean, types, None
# Functions, modules, classes, compiled code, stack tracebacks

i = 5
i + i

len(str(10 ** 1000))
print(len(str(10 ** 1000)))

print(len(str(math.pi)))
math.sqrt(6000)
random.random()


x = i


S = 'Spam'
len(S)
S[0]
S[1]
S[-1]
S[-2]
S[len(S)-1] #The Hard Way

print(S, S[0:4])
print(S[0:4])
print(S[0:len(S)])
print(len(S))
print(S, S+'my', S*10)
S = S +'my'
print(S)
S = 'Shrubbery' #bytearray type
L = list(S)
print(L)
L[1] = 'c'
print(L)
''.join(L)
print(L, type(L), ''.join(L))
L = ''.join(L)
print(L, type(L))

B = bytearray(b'spam') #bytearray type
print(B, type(B)) #b'spam' is for bytearray
print(len(B))
Bb = 'spam'
B.extend(b'eggs')
print(B)
print(B.decode())
print(B)
print(B)
print('fuck salt')

#Find the offset of a substring in S
S = 'Spam'
S.find('pa')
print(S.find('pa'))
line = 'aaa,bbb,ccc,ddd'
line = line.split(',')
print(line)

line = 'aaa,ccc,bbb,dddd'
print(type(line), type(line.split(',')))
S = 'spam'
S = S.upper()
S = S.replace('am', 'ack')
print(S, S.isalpha(), S.isdigit())
line = 'aaa,bbb,cccc,dd\n'
print(line, '\n\n\n\n', line.rstrip())
print(line.split(','), line.rstrip().split(','))

#formatting expressions
hey = '% %'.format('fuck', 'salt')
print(hey)
hey = '%s %s'.format('fuck', 'salt')
print(hey, type(hey))
kegg = '{0} this is some {1}'.format('bull', 'shit')
print(kegg, type(kegg))
chegg = '{} this is some {}'.format('some', 'balaclava')
print(chegg, type(chegg))

h = '{:,.2f}'.format(234324.23323423)
h = '{:,.2f}'.format(234324.23323423)
print(h, type(h))
y = '%.2f | %+05d' % (3.1415, -42)
print(y, type(y))
dir(y)
print(dir(y))

raw = """
hellow
my


friend
            j"""
print(raw, type(raw))
raw = '''
lets



have fun     in the     sun
'''
print(raw)
print(raw)


print(u'sp/u00c4m')
u'sp/u00c4m'
print(u'sp/uOOc4m')

#Lists
L = [123, 44.112211212, 'fucksalt']
L.append('NI')
print(L)
L.append('NI')
print(L)
L.pop()
L.pop()
L.append(1)
L.append('NI')
dir(L.append)

print(L)
print(L, L.pop(), L.pop(), L.pop(), L.pop(), L.pop(), type(L))
L = [1, 2, 3, 4, 5, 6, 'string']
print(type(L[0]), type(L[:]), type(L[-1]), L[-1])
print(L[0:-1])
print(L.pop(0))
print(L)
L.append('fucksalt')

L.pop()
print(L, type(L))
L.pop()
print(L)
print(type(L), type(L[1]), len(L), type(L[4]))

#Nesting and Matrices
M = [[1,2,3],
     [4,5,6],
     [7,8,9], 1]
print(M, type(M), M.pop())
print(M[0])
print(M[0][0])
print(type(M[0][0]))
print(M[-1][-1])
print(M[0][1])
print(M[-1][2])
print('\n\n\n\n')
# print(M[0][0],M[0][1],M[0][2], M[1][0], M[1][1], M[1][2], M[2][0], M[2][1], M[2][2])

print(M, len(M), len(M[0]), len(M[1]), len(M[2]), len(M[:][:]))
#This is a list comprehension

col2 = [row[1] for row in M] #give me row[1] for each row in matrix M, in a new list called col2
print(col2, type(col2), len(col2))
col3 = [cha[2] for cha in M]
print(col3)
col3 = [row[1] + 1 for row in M]
print(col3)
no_odd = [row[1] for row in M if row[1] % 2 == 0]
print(no_odd)


#advanced comprehension
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c*2 for c in 'spam']
print(doubles)
doubles = [anythingcangohere*5 for anythingcangohere in 'sammyboy']
print(doubles)
comprehension = [i*44 for i in 'foo'] #give me i*44 for each i in 'foo', as a variable called comprehension
print(comprehension)

#lists and ranges

list(range(4))
print(list(range(4)), len(list(range(4))), list(range(0,10,2)))


x = [[x**2, x**3]for x in range(4)]
print(x, type(x))
x.append('hello')
print(x)
print(x[4])

foo = [[x*x*x, x/4, x*5/2] for x in range(0,10,3) if x<5 ]
print(foo)

#this is a generator; like a comprehension but enclosed in parenthases "()"
G = (sum(row) for row in M)
print(G)
print(type(G))
help(G)

print(G, next(G), next(G), next(G))

print(list(map(sum,M)))

#A map
print(type(list(map(sum,M))))
print({sum(row) for row in M})
#key-value table of row sums
foo = {i : sum(M[i]) for i in range(3)}
print(foo)
rec = {'name': {'first': 'Bob', 'First' : 'list'}}
print(rec,rec['name'], rec['name']['first'])

#its a tuple
T = (1,2,3,4,5)
print(T)
print(T + (5,6,7,8,9))
T.index(5)
print(T.index(5))



# Test test 1,2,3
L = [1,2,3,4,5]
print(type(L), type(type(L)), type(L) == type([]))

foo = 'test'

if isinstance(foo, str):
    print('true')

#CLASSES
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return print(self.name.split()[-1])
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


Sam = Worker('Sam Petzold', 140000)
Yifan = Worker('Yifan Li', 200000)

Sam.lastName()

floats = [3.14156789101112, 3.14E-34, 3E210, 4.0e+210]
print(floats, type(floats), type(floats[:]), len(floats))


print(1/3+2/3)
x = 1/3 + 2/3
print('{0:4.20f}'.format(x))
print(x < 1.0000000000, x > 1.0000000000, x == 1)

x = 6
y = 5
print(x/y, x//y)

#in python truncate != floor
a = math.floor(2.5)
b = math.floor(-2.5)
c = math.trunc(2.5)
d = math.trunc(-2.5)
print(a,b,c,d)


print(math.pi, math.e)
print(math.sin(2*math.pi/180), math.sqrt(144), math.sqrt(2), pow(2,4), abs(-23), sum((1,2,3,4,5)), min(233,1), max(233, 4))
#floor is go to next lower integer
#truncate is drop decimal digits
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))


print(random.random(), random.randint(1, 10), random.randint(1,10))

foo = ['once', 'there', 'was', 'a', 'dull', 'boy']
print(random.choice(foo))
print(random.shuffle(foo))
print(foo)

#objects have more structure than just enough space to represent their values each object also has two standard header fields:
# a "type designator" used to marke the TYPE of the object
# reference counter used to determine when its ok to reclaim the object. To understand these two headers fields factor into the model, we
# In C Pointers are memory addresses. but reerences are implemented as pointers and serve the same role
# you can never actually do anything usefull with a reference itself. eliminates a vast category of C bugs. Think of Python references as C "void" ointers, which are automatically folowed whenever used
# Types live with objects, not variables.
print(type(foo))
classmethod(foo)
print(classmethod(foo))
print(L)
print(L.append(L))
print(type(L.append(L)))


repr('hellomyname')
print(repr(234))
print(type(repr(234)))
print( chr(115))


S = 'spam'
S = S +'spam'
print(S)
S = 'splot'
S = S.replace('pl','foo')
print(S)
'This is %s %s'.format('bull', 'shit')
print('%s %s %d'.format('bull', 'shit', 48), '%s %s %d' % ('bull', 'shit', 48), 'This is {} {}'.format('bull','shit'), '{0} {1}'.format('kill', 'them'))
A = 'foo'
B = 73.23423
print('{0} {1}'.format(A, B))




S = 'spam'
print(S.find('sp'))

template = '{0} {1} {2} {3}'
cha = template.format('hello', 'what', 'is', 'it')
print(cha)
for x in cha: print(x)
foo = 'lets go outside and get a burger'
for x in foo: print(foo)
for x in foo: print(x)

L = [x**2 for x in range(5)]
print(L)
print(['Nein'] * 8)

for x in [1,2,3]: print(x)
for x in [1,2,3,[4,5]]: print(x)
foo = [1,2,3,[4,5]]

name = dict(first = 'bob', last ='smith')
rec = dict(name=name, job=['dev', 'mgr' ], age=40.5)
print(rec)

json.dumps(rec)
S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)
print(O == rec)

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())

P = json.load(open('testjson.txt'))
P
print(P)
#
# rdr = csv.reader(open('csvdata.txt'))
# for row in rdr: print(row)

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('>i4sh', data)
print(values)
dir(print())
print(dir(print()))

# the == operator tsts value equivalence python performs and equivalence test, comparing all nexsted objects recursively
#the is oeprator tests object identity python test whether the two are really the same object
#Dictionaries are eqal if their sorted (key, value) lists are equal.

print(True == abs(-1))

#This is a generator function

def gen(n):
    for i in n:
        print(n)
        yield i*2

#This is a namespace
x = 'old'
def function():
    global x, y; x = 'new'

def outer():
    x = 'old'
    def function():
        nonlocal x; x = 'new'

# class SubClass(Superclass):

#     staticData = []
#     def method(self): pass
#

x = [1,2,3]
print(x)

# while True:
#     reply = input('Input here:')
#     if reply == 'stop': break
#     print(reply.upper())


# while True:
#     reply = input('input here:')
#     if reply == 'stop': break
#     print(reply)
#

# while True:
#     reply = input('hello')
#     if reply == 'stop': pass
#     print(reply)
#

# while True:
#     reply = input('Input Here')
#     if reply == 'stop':
#         print('have an ice day')
#         break
#     try:
#         print(float(reply))
#     except:
#         print('bad bad bad bad bad bad bad')





























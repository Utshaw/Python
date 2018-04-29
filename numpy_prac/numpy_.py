

import numpy

l = [1, 2, 3, 4]

n = numpy.array(l)
n2 = numpy.array([5, 6, 2, 4])

print(n * 2)

print(n ** 2)

print(n + n2)

a = numpy.array([1, 2])
b = numpy.array([2, 1])

print(a.dot(b))

print(numpy.dot(a, b))

print(numpy.sqrt(numpy.sum(a ** 2)))

print(numpy.linalg.norm(a))


cosangle = a.dot(b) / (numpy.linalg.norm(a) * numpy.linalg.norm(b))

angle = numpy.arccos(cosangle)

print(angle)  # in radians

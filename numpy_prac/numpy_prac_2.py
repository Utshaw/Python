import numpy

A = numpy.array([[1, 2], [3, 4]])


Ainv = numpy.linalg.inv(A)

print(Ainv)


print(Ainv.dot(A)) # matrix multiplication

print(numpy.linalg.det(A))

print(numpy.diag(A))

print(numpy.diag([3, 4]))


a = numpy.array([1, 2])

b = numpy.array([3, 4])

print(numpy.outer(a, b)) # outer product

print(numpy.inner(a, b)) # inner product

print(numpy.trace(A)) # trace of matrix

X = numpy.random.randn(100, 3)

print(X)


print(numpy.cov(X.T)) # covariance
















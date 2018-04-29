import numpy

A = numpy.array([[1, 2], [3, 4] ])


B = numpy.array([3, 4])

print(numpy.linalg.inv(A).dot(B))

print(numpy.linalg.solve(A, B)) # more accurate & better aooriach to solve a system of linear equations







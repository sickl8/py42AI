from matrix import Matrix

mrx = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
print(mrx.data)
print(mrx.shape)
mrx = Matrix((3, 4))
print(mrx.data)
print(mrx.shape)
mrx = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],(3, 3))
print(mrx.data)
print(mrx.shape)
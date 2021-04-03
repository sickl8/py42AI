from matrix import Matrix
from vector import Vector

def test(stg):
	print(str('\nTest ' + stg + ' ').ljust(20, '-') + '\n')

def print_oper(a0, op, a1, a2):
    lenj = max(len(str(a0)), len(str(a1)), len(str(a2))) + 3
    print(str(a0).rjust(lenj, ' '))
    print(op)
    print(str(a1).rjust(lenj, ' '))
    print(''.rjust(lenj, '-'))
    print(str(' = ' + str(a2)).rjust(lenj, ' '))

mtx = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
print(mtx.data)
print(mtx.shape)
mtx = Matrix((3, 4))
print(mtx.data)
print(mtx.shape)
mtx = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],(3, 3))
print(mtx.data)
print(mtx.shape)
test('mtx + vec')
mtx = Matrix([[4.0], [5.0], [6.0], [7.0]])
vec = Vector([0.0, 1.0, 2.0, 3.0])
print('Matrix shape: ' + str(mtx.shape))
print('Vector shape: ' + str((vec.size, 1)))
res = mtx + vec
print_oper(mtx, ' + ', vec, res)
test('mtx + mtx')
mtx0 = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
mtx1 = Matrix([[4.0, 5.0, 6.0, 7.0], [0.0, 1.0, 2.0, 3.0]])
res = mtx0 + mtx1
print_oper(mtx0, ' + ', mtx1, res)
test('mtx - vec')
mtx = Matrix([[4.0], [5.0], [6.0], [7.0]])
vec = Vector([0.0, 1.0, 2.0, 3.0])
res = mtx - vec
print_oper(mtx, ' - ', vec, res)
test('mtx - mtx')
mtx0 = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
mtx1 = Matrix([[4.0, 5.0, 6.0, 7.0], [0.0, 1.0, 2.0, 3.0]])
res = mtx0 - mtx1
print_oper(mtx0, ' - ', mtx1, res)
test('mtx / sca')
mtx0 = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
sca = 2
res = mtx0 / sca
print_oper(mtx0, ' / ', sca, res)
test('mtx * sca')
mtx0 = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
sca = 2
res = mtx0 * sca
print_oper(mtx0, ' * ', sca, res)
test('mtx * vec')
mtx = Matrix([[0.0, 1.0, 2.0, 3.0],
			  [4.0, 5.0, 6.0, 7.0]])
vec = Vector([0.0, 1.0, 2.0, 3.0])
print('mtx shape = ', mtx.shape, '\nvec shape = ', vec.shape)
res = mtx * vec
print_oper(mtx, ' * ', vec, res)
test('mtx * mtx')
mtx0 = Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
mtx1 = Matrix([[4.0, 5.0, 6.0, 7.0, 4.0, 5.0, 6.0, 7.0],
			   [0.0, 1.0, 2.0, 3.0 ,4.0, 5.0, 6.0, 7.0],
			   [4.0, 5.0, 6.0, 7.0, 4.0, 5.0, 6.0, 7.0],
			   [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]])
print('mtx0 shape = ', mtx0.shape, '\nmtx1 shape = ', mtx1.shape)
res = mtx0 * mtx1
print_oper(mtx0, ' * ', mtx1, res)

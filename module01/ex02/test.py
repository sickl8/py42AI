from vector import Vector
import decimal


def drange(*args):
    x = args[0] if len(args) >= 2 else 0
    y = args[0] if len(args) == 1 else args[1] if len(args) >= 2 else 0
    jump = args[2] if len(args) == 3 else 1
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)


def frange(*args):
    if len(args) == 1:
        return list(drange(args[0]))
    elif len(args) == 2:
        return list(drange(args[0], args[1]))
    elif len(args) == 3:
        return list(drange(args[0], args[1], args[2]))
    return list()


def print_banner(srg):
    print()
    print(srg.ljust(20 + len(srg), '|').rjust(40 + len(srg), '|'))
    print()


def print_oper(a0, op, a1, a2):
    lenj = max(len(str(a0)), len(str(a1)), len(str(a2))) + 3
    print(str(a0).rjust(lenj, ' '))
    print(op)
    print(str(a1).rjust(lenj, ' '))
    print(''.rjust(lenj, '-'))
    print(str(' = ' + str(a2)).rjust(lenj, ' '))


vec = Vector((10, 16))
print('vec = Vector((10, 16)): ' + str(vec))
vec = Vector(0)
print('vec = Vector(0): ' + str(vec))
vec = Vector([2.0, 3.0, 8, 7.0])
print('vec = Vector([2.0, 3.0, 8.0, 7.0]): ' + str(vec))
vec = Vector([1, 2, 3, 4])
print_banner(' vec + vec = vec ')
vec0 = Vector((5, 10))
vec1 = Vector((6, 11))
vec2 = vec0 + vec1
print_oper(vec0.values, ' + ', vec1.values, vec2.values)
print_banner(' vec + sca = vec ')
vec0 = Vector((5, 10))
sca = 5
vec1 = vec0 + sca
print_oper(vec0.values, ' + ', sca, vec1.values)
print_banner(' vec - vec = vec ')
vec0 = Vector((5, 10))
vec1 = Vector((6, 11))
vec2 = vec0 - vec1
print_oper(vec0.values, ' - ', vec1.values, vec2.values)
print_banner(' vec - sca = vec ')
vec0 = Vector((5, 10))
sca = 5
vec1 = vec0 - sca
print_oper(vec0.values, ' - ', sca, vec1.values)
print_banner(' vec * vec = sca ')
vec0 = Vector((5, 10))
vec1 = Vector((6, 11))
res = vec0 * vec1
print_oper(vec0.values, ' * ', vec1.values, res)
print_banner(' vec * sca = vec ')
vec0 = Vector((5, 10))
sca = 5
vec1 = vec0 * sca
print_oper(vec0.values, ' * ', sca, vec1.values)
print_banner(' vec / sca = vec ')
vec0 = Vector((5, 10))
sca = 5
vec1 = vec0 / sca
print_oper(vec0.values, ' / ', sca, vec1.values)

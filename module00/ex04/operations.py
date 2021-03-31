import sys


def usage():
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('    python operations.py 10 3')


argc = len(sys.argv)
if (argc <= 1):
    usage()
    exit()
elif (argc > 3):
    print('InputError: too many arguments\n')
    usage()
    exit()
elif (not (sys.argv[1].isnumeric() and sys.argv[2].isnumeric())):
    print('InputError: only numbers\n')
    usage()
    exit()
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print('Sum:         ' + str(num1 + num2))
print('Difference:  ' + str(num1 - num2))
print('Product:     ' + str(num1 * num2))
print('Quotient:    ', end='')
if (num2 == 0):
    print('ERROR (div by zero)')
else:
    print(str(num1 / num2))
print('Remainder:   ', end='')
if (num2 == 0):
    print('ERROR (modulo by zero)')
else:
    print(str(num1 % num2))

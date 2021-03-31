import sys

if len(sys.argv) <= 1:
    exit()
if len(sys.argv) > 2 or len(sys.argv) == 2 and not sys.argv[1].isnumeric():
    print('ERROR')
    exit()
num = int(sys.argv[1])
if num == 0:
    print("I'm Zero")
elif num % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")

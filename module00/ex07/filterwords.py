import sys
import string


def remove_string():
    for itr in chain:
        if len(itr) <= minl:
            chain.remove(itr)
            return False
    return True


argc = len(sys.argv)
if argc != 3 or not sys.argv[2].isnumeric() or sys.argv[1].isnumeric():
    print('ERROR')
    exit()
chain = sys.argv[1].split()
minl = int(sys.argv[2])
for itr in range(0, len(chain)):
    for c in string.punctuation:
        chain[itr] = chain[itr].replace(c, '')
bol = False
while not bol:
    bol = remove_string()
print(chain)

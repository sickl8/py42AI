import sys

string = ""
if len(sys.argv) > 2:
    for i in range(1, len(sys.argv) - 1):
        string += sys.argv[i]
        string += " "
    string += sys.argv[i+1]
elif len(sys.argv) > 1:
    string = sys.argv[1]
string2 = string[::-1]
print(string2.swapcase())

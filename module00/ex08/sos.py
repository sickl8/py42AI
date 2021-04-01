import sys

argc = len(sys.argv)
if argc <= 1:
    exit()

strr = ''
for itr in sys.argv[1:]:
    strr += itr.upper()
    strr += ' '
words = strr.split()
for itr in words:
    if not itr.isalnum():
        print('ERROR')
        exit()
dic = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
     }

nwrd = len(words)
for i in range(0, nwrd):
    wlen = len(words[i])
    for j in range(0, wlen):
        print(dic[words[i][j]], end='')
        if j < wlen - 1:
            print(' ', end='')
    if i < nwrd - 1:
        print(' / ', end='')
print('')

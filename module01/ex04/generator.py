from random import randint


def generator(text: str, sep=" ", option=None):
    if (type(text) != str or type(sep) != str or type(option) == str and
       (option == 'shuffle' or option == 'ordered' or option == 'unique')):
        yield 'ERROR'
        return
    words = text.split(sep)
    if option == 'ordered':
        words.sort()
    elif option == 'unique':
        words = list(dict.fromkeys(words))
    elif option == 'shuffle':
        for _ in range(2 * len(words)):
            num1 = randint(0, len(words) - 1)
            num2 = randint(0, len(words) - 1)
            stg = words[num1]
            words[num1] = words[num2]
            words[num2] = stg
    for word in words:
        yield word
    return

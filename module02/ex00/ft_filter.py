class Filter:
    itered = False

    def __init__(self):
        self.lst = []

    def __iter__(self):
        self.index = 0
        return self

    def append(self, var):
        self.lst.append(var)

    def __next__(self):
        if self.itered or self.index >= len(self.lst):
            self.itered = True
            raise StopIteration
        ret = self.lst[self.index]
        self.index += 1
        return ret


def ft_filter(function_to_apply, list_of_inputs):
    pass
    lst = Filter()
    for elem in list_of_inputs:
        if function_to_apply(elem):
            lst.append(elem)
    return lst


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
filtered_vowels = ft_filter(filter_vowels, letters)
print(type(filtered_vowels))
print(filtered_vowels)
for i in filtered_vowels:
    print('once ', i)
for i in filtered_vowels:
    print('twice ', i)

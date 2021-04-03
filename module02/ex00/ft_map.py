class Map:
    iter = False

    def __init__(self):
        self.values = []

    def append(self, var):
        self.values.append(var)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.iter is True or self.index >= len(self.values):
            self.iter = True
            raise StopIteration
        ret = self.values[self.index]
        self.index += 1
        return ret


def ft_map(function_to_apply, list_of_inputs):
    pass
    obj = Map()
    for elem in list_of_inputs:
        obj.append(function_to_apply(elem))
    return obj


def myfunc(a):
    return len(a)


x = ft_map(myfunc, ('apple', 'banana', 'cherry'))
y = map(myfunc, ('apple', 'banana', 'cherry'))

print(y)
print(x)
print(list(y))
print(list(x))
for i in x:
    print('x ' + str(i))
for i in y:
    print('y ' + str(i))

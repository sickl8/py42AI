import functools


def ft_reduce(function_to_apply, list_of_inputs):
    it = iter(list_of_inputs)
    value = next(it)
    for element in it:
        value = function_to_apply(value, element)
    return value


lis = [1, 3, 5, 6, 2]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
print("The sum of the list elements is : ", end="")
print(ft_reduce(lambda a, b: a + b, lis))
print("The maximum element of the list is : ", end="")
print(ft_reduce(lambda a, b: a if a > b else b, lis))

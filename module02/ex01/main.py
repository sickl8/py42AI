def what_are_the_vars(*args, **kwargs):
    """Your code"""
    pass
    ret = ObjectC()
    for key in kwargs.keys():
        if key.find('var_') == 0 and key[4:].isnumeric() is True:
            return None
    ret.__dict__.update(**kwargs)
    i = 0
    for val in args:
        ret.__dict__.update({'var_' + str(i): val})
        i += 1
    return ret


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

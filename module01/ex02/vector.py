import itertools


class Vector:
    values = []
    size = 0
    shape = ()

    def init_from_list(self, values):
        self.values = []
        for val in values:
            self.values.append(float(val))
        self.size = len(values)
        self.shape = (self.size, 1)

    def init_from_tupl(self, tupl):
        self.values = []
        for i in range(tupl[0], tupl[1]):
            self.values.append(float(i))
        self.size = len(self.values)
        self.shape = (self.size, 1)

    def init_from_size(self, size):
        self.init_from_tupl((0, size))

    def __init__(self, var):
        if (type(var) is tuple and len(var) == 2 and all(type(num) is int
           for num in var) and var[0] <= var[1]):
            self.init_from_tupl(var)
        elif (type(var) is list and all(type(membr) is float or type(membr)
              is int for membr in var)):
            self.init_from_list(var)
        elif type(var) is int and var >= 0:
            self.init_from_size(var)
        else:
            raise Exception('Vector can only be initilized from a tuple(min: i\
nt, max: int), a positive integer as a size, or a list of floats.')

    def __str__(self):
        return '(Vector ' + str(self.values) + ')'

    def __repr__(self):
        return self.__str__()

    def add_vector(self, vec):
        if self.size != vec.size:
            raise Exception('Operation on vectors with different sizes')

        ret = Vector(self.values)
        for i in range(0, ret.size):
            ret.values[i] += vec.values[i]
        return ret

    def add_scalar(self, scalar):
        ret = Vector(self.values)
        scalar = float(scalar)
        for i in range(0, ret.size):
            ret.values[i] += scalar
        return ret

    def handle_add(self, var):
        if (type(var) is not Vector and
           type(var) is not float and type(var) is not int):
            raise Exception('Invalid addition')

        elif type(var) is Vector:
            return self.add_vector(var)
        return self.add_scalar(var)

    def __add__(self, var):
        return self.handle_add(var)

    def __radd__(self, var):
        return self.handle_add(var)

    def sub_vector(self, vec):
        ret = Vector(self.values)
        if ret.size != vec.size:
            raise Exception('Operation on vectors with different sizes')

        for i in range(0, ret.size):
            ret.values[i] -= vec.values[i]
        return ret

    def sub_scalar(self, scalar):
        ret = Vector(self.values)
        scalar = float(scalar)
        for i in range(0, ret.size):
            ret.values[i] -= scalar
        return ret

    def handle_sub(self, var):
        if (type(var) is not Vector and
           type(var) is not float and type(var) is not int):
            raise Exception('Invalid subtraction')

        elif type(var) is Vector:
            return self.sub_vector(var)
        return self.sub_scalar(var)

    def __sub__(self, var):
        return self.handle_sub(var)

    def __rsub__(self, var):
        return self.handle_sub(var)

    def mul_vector(self, vec):
        ret = 0.0
        if self.size != vec.size:
            raise Exception('Operation on vectors with different sizes')

        for i in range(0, self.size):
            ret += self.values[i] * vec.values[i]
        return ret

    def mul_scalar(self, scalar):
        ret = Vector(self.values)
        scalar = float(scalar)
        for i in range(0, ret.size):
            ret.values[i] *= scalar
        return ret

    def handle_mul(self, var):
        if (type(var) is not Vector and
           type(var) is not float and type(var) is not int):
            raise Exception('Invalid multiplication')

        elif type(var) is Vector:
            return self.mul_vector(var)
        return self.mul_scalar(var)

    def __mul__(self, var):
        return self.handle_mul(var)

    def __rmul__(self, var):
        return self.handle_mul(var)

    def truediv_scalar(self, scalar):
        scalar = float(scalar)
        ret = Vector(self.values)
        if scalar == 0:
            raise Exception('Vector division by Zero')
        for i in range(0, ret.size):
            ret.values[i] /= scalar
        return ret

    def handle_truediv(self, var):
        if type(var) is not float and type(var) is not int:
            raise Exception('Invalid division')

        return self.truediv_scalar(var)

    def __truediv__(self, var):
        return self.handle_truediv(var)

    def __rtruediv__(self, var):
        return self.handle_truediv(var)

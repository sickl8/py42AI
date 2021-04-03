from vector import Vector


class Matrix:
    data = []
    shape = ()

    def init_from_shape(self, shape):
        self.data = []
        for _ in range(shape[0]):
            self.data.append([])
            for _ in range(shape[1]):
                self.data[-1].append(float(0))
        self.shape = shape

    def init_from_llist(self, lst):
        self.data = []
        for i in range(0, len(lst)):
            self.data.append([])
            for j in range(0, len(lst[i])):
                self.data[-1].append(float(lst[i][j]))
        self.shape = (len(lst), len(lst[0]))

    def good_llist(self, lst):
        if (type(lst) == list and len(lst) > 0 and all(type(subl) == list and
           len(subl) > 0 and all(type(mbr) == int or type(mbr) == float
           for mbr in subl) for subl in lst)):
            sub_len = len(lst[0])
            if all(len(subl) == sub_len for subl in lst):
                return True
        return False

    def good_shape(self, shape):
        if (type(shape) == tuple and len(shape) == 2 and all(type(mbr) == int
           and mbr > 0 for mbr in shape)):
            return True
        return False

    def __init__(self, var, shape=None):
        if self.good_llist(var) and shape is None:
            self.init_from_llist(var)
        elif self.good_shape(var) and shape is None:
            self.init_from_shape(var)
        elif (shape and self.good_shape(shape) and
              self.good_llist(var) and len(var) == shape[0] and
              len(var[0]) == shape[1]):
            self.init_from_llist(var)
        else:
            print('invalid matrix args')
            exit()

    def matrix_addition(self, mtx):
        ret = Matrix(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.data[i][j] = self.data[i][j] + mtx.data[i][j]
        return ret

    def __add__(self, var):
        if (type(var) == Vector and var.size == self.shape[0]
           and self.shape[1] == 1):
            lst = []
            for elem in var.values:
                lst.append([elem])
            mtx = Matrix(lst)
            return self.matrix_addition(mtx)
        elif (type(var) == Matrix and var.shape[0] == self.shape[0]
              and var.shape[1] == self.shape[1]):
            return self.matrix_addition(var)
        raise Exception('Invalid opreand for Matrix Operation')

    def __radd__(self, var):
        return self.__add__(var)

    def matrix_subtraction(self, mtx0, mtx1):
        ret = Matrix(mtx0.shape)
        for i in range(mtx0.shape[0]):
            for j in range(mtx0.shape[1]):
                ret.data[i][j] = mtx0.data[i][j] - mtx1.data[i][j]
        return ret

    def __sub__(self, var):
        if (type(var) == Vector and var.size == self.shape[0]
           and self.shape[1] == 1):
            lst = []
            for elem in var.values:
                lst.append([elem])
            mtx = Matrix(lst)
            return self.matrix_subtraction(self, mtx)
        elif (type(var) == Matrix and var.shape[0] == self.shape[0]
              and var.shape[1] == self.shape[1]):
            return self.matrix_subtraction(self, var)
        raise Exception('Invalid opreand for Matrix Operation')

    def __rsub__(self, var):
        if (type(var) == Vector and var.size == self.shape[0]
           and self.shape[1] == 1):
            lst = []
            for elem in var.values:
                lst.append([elem])
            mtx = Matrix(lst)
            return self.matrix_subtraction(mtx, self)
        elif (type(var) == Matrix and var.shape[0] == self.shape[0]
              and var.shape[1] == self.shape[1]):
            return self.matrix_subtraction(mtx, self)
        raise Exception('Invalid opreand for Matrix Operation')

    def matrix_tdiv(self, var):
        var = float(var)
        ret = Matrix(self.data)
        if var == 0:
            raise Exception('Matrix divison by Zero')
        for i in range(ret.shape[0]):
            for j in range(ret.shape[1]):
                ret.data[i][j] /= var
        return ret

    def __truediv__(self, var):
        if (type(var) == int or type(var) == float):
            return self.matrix_tdiv(var)
        raise Exception('Invalid opreand for Matrix Operation')

    def __rtruediv__(self, var):
        raise Exception('Cannot divide a scalar by a Matrix')

    def matrix_mul_scalar(self, sca):
        ret = Matrix(self.data)
        for i in range(ret.shape[0]):
            for j in range(ret.shape[1]):
                ret.data[i][j] *= sca
        return ret

    def abs_compatible_matrix(self, var):
        if (type(var) == Matrix and var.shape[0] == self.shape[0] and
           var.shape[1] == self.shape[1]):
            return True
        return False

    def compatible_matrix(self, mtx0, mtx1):
        if (type(mtx0) == Matrix and type(mtx1) == Matrix
           and mtx0.shape[1] == mtx1.shape[0]):
            return True
        return False

    def matrix_mul_matrix(self, mtx0, mtx1):
        ret = Matrix((mtx0.shape[0], mtx1.shape[1]))
        ln = mtx0.shape[1]
        for i in range(ret.shape[0]):
            for j in range(ret.shape[1]):
                for k in range(ln):
                    ret.data[i][j] = mtx0.data[i][k] * mtx1.data[k][j]
        return ret

    def matrix_mul_vector(self, mtx0, mtx1):
        ret = self.matrix_mul_matrix(mtx0, mtx1)
        lst = []
        for elem in ret.data:
            lst.append(elem[0])
        ret = lst
        return ret

    def __mul__(self, var):
        if (type(var) == int or type(var) == float):
            return self.matrix_mul_scalar(var)
        elif self.compatible_matrix(self, var):
            return self.matrix_mul_matrix(self, var)
        elif type(var) == Vector:
            lst = []
            for elem in var.values:
                lst.append([elem])
            var = Matrix(lst)
            if self.compatible_matrix(self, var):
                return self.matrix_mul_vector(self, var)
        raise Exception('Invalid opreand for Matrix Operation')

    def __rmul__(self, var):
        if self.compatible_matrix(var, self):
            return self.matrix_mul_matrix(self, var)
        elif type(var) == Vector:
            lst = []
            for elem in var.values:
                lst.append([elem])
            var = Matrix(lst)
            if self.compatible_matrix(var, self):
                return self.matrix_mul_vector(var, self)
        raise Exception('Invalid opreand for Matrix Operation')

    def __str__(self):
        return '(Matrix ' + str(self.data) + ')'

    def __repr__(self):
        return self.__str__()

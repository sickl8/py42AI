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

    def	good_shape(self, shape):
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
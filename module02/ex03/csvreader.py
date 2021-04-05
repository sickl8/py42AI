class CsvReader():
    filename = None
    file = None
    header = None
    data = None
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        pass
        if filename is None or type(filename) != str:
            return
        self.filename = filename
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            self.filename = None
            self.file = None
            return
        lines = self.file.read().split('\n')
        if lines[-1] == '':
            lines.pop(-1)
        self.data = []
        for line in lines:
            self.data.append(line.split(sep))
        for i in range(0, skip_top):
            self.data.pop(0)
        for i in range(0, skip_bottom):
            self.data.pop(-1)
        if header is True:
            self.header = self.data[0]
            self.data.pop(0)

    def get_data(self):
        return self.data

    def get_header(self):
        return self.header

    def __enter__(self):
        if self.file and len(self.data) > 0:
            ln = len(self.data[0])
            for lst in self.data:
                if len(lst) != ln:
                    self.filename = None
                    return None
        elif self.file is None:
            return None
        return self

    def __exit__(self, *exc):
        if self.file:
            print('closed fd')
            self.file.close()
        return


class ContextManager():
    def __init__(self):
        print('init method called')
    def __enter__(self):
        print('enter method called')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with CsvReader('addresses.csv') as file:
    if file == None:
        print("File is corrupted")
    else:
        data = file.get_data()
        header = file.get_header()
        print('header = ', header)
        print('data = ', data)
    # print('with statement block')
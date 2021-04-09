import shlex
# from tabulate import tabulate


class CsvReader():
    filename = None
    file = None
    header = None
    data = None
    valid = True

    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        pass
        if filename is None or type(filename) != str:
            return
        self.filename = filename
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            self.valid = False
            return
        lines = self.file.read().split('\n')
        if lines[-1] == '':
            lines.pop(-1)
        self.data = []
        for line in lines:
            lst = []
            slc_start = 0
            i = 0
            line += '\0'
            while i < len(line):
                while i < len(line) and line[i] != sep:
                    while i < len(line) and line[i] == '"':
                        i += 1
                        while i < len(line) and line[i] != '"':
                            i += 1
                        if i == len(line):
                            self.valid = False
                            return
                        if i < len(line):
                            i += 1
                    if i < len(line) and line[i] != sep:
                        i += 1
                if i < len(line):
                    toappend = line[slc_start:i].replace('"', '')
                    toappend = toappend.replace('\0', '').strip()
                    lst.append(toappend)
                    if line[i] == sep:
                        i += 1
                    slc_start = i
                elif i == len(line):
                    toappend = line[slc_start:i].replace('"', '')
                    toappend = toappend.replace('\0', '').strip()
                    lst.append(toappend)
            self.data.append(lst)
        if self.file and len(self.data) > 0:
            ln = len(self.data[0])
        for lst in self.data:
            if len(lst) != ln:
                self.valid = False
                return
        if header is True:
            self.header = self.data[0]
            self.data.pop(0)
        for i in range(0, skip_top):
            self.data.pop(0)
        for i in range(0, skip_bottom):
            self.data.pop(-1)

    def get_data(self):
        return self.data

    def get_header(self):
        return self.header

    def __enter__(self):
        if self.valid is False:
            return None
        return self

    def __exit__(self, *exc):
        if self.file:
            self.file.close()
        return


# with CsvReader('addresses.csv', header=True) as file:
#     if file is None:
#         print("File is corrupted")
#     else:
#         data = file.get_data()
#         header = file.get_header()
#         print(tabulate(data, headers=header, tablefmt='orgtbl'))

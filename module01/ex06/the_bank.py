class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
            Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def good_account(self, account):
        if type(account) != Account:
            return False
        atr_lst = dir(account)
        if len(atr_lst) % 2 == 0:
            return False
        if any(atr.find('b') == 0 for atr in atr_lst):
            return False
        if not any(atr.find('zip') == 0 or atr.find('addr') == 0
           for atr in atr_lst):
            return False
        if ('name' not in atr_lst or 'id' not in atr_lst or
           'value' not in atr_lst):
            return False
        return True

    def search_by_name(self, name):
        for i in range(len(self.account)):
            if hasattr(self.account[i], 'name'):
                if self.account[i].name == name:
                    return i
        return None

    def search_by_id(self, id):
        for i in range(len(self.account)):
            if hasattr(self.account[i], 'id'):
                if self.account[i].id == id:
                    return i
        return None

    def transfer(self, origin, dest, amount):
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return         True if success, False if an error occured
        """
        if type(amount) != float or amount < 0:
            return False
        if type(origin) != str and type(origin) != int:
            return False
        if type(dest) != str and type(dest) != int:
            return False
        acc0 = None
        acc1 = None
        if type(origin) == str:
            acc0 = self.search_by_name(origin)
        else:
            acc0 = self.search_by_id(origin)
        if type(dest) == str:
            acc1 = self.search_by_name(dest)
        else:
            acc1 = self.search_by_id(dest)
        if (acc0 is None or acc1 is None or
           not self.good_account(self.account[acc0]) or
           not self.good_account(self.account[acc1])):
            return False
        if self.account[acc0].value < amount:
            return False
        self.account[acc0].transfer(-amount)
        self.account[acc1].transfer(amount)
        return True

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        index = None
        if type(account) == int:
            index = self.search_by_id(account)
        elif type(account) == str:
            index = self.search_by_name(account)
        else:
            return False
        if index is None:
            return False
        atr_lst = dir(self.account[index])
        for i in range(len(atr_lst)):
            if atr_lst[i].find('b') == 0:
                atr_lst[i][0] = 'd'
        if 'name' not in atr_lst and 'id' in atr_lst:
            self.account[index].__dict__.update
            ({'name': 'acc_id:' + str(self.account[index].id)})
        elif 'name' in atr_lst and 'id' not in atr_lst:
            self.account[index].__dict__.update
            ({'id': Account(self.account[index].name).id})
        if 'value' not in atr_lst:
            self.account[index].__dict__.update({'value': 0})
        if (not any(atr.find('zip') == 0 or atr.find('addr') == 0
           for atr in atr_lst)):
            self.account[index].__dict__.update({'zip': ''})
        if len(atr_lst) % 2 == 0:
            self.account[index].__dict__.update({'additional': None})
        if self.good_account(self.account[index]):
            return True
        return False

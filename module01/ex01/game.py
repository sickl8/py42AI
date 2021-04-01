class GotCharacter:
    first_name = ''
    is_alive = True

    def __init__(self, first_name, is_alive=True):
        if not isinstance(first_name, str) or first_name == '':
            print('First name should be a non-empty string')
            exit()
        if not isinstance(is_alive, bool):
            print('Is_alive should be a boolean')
            exit()
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to goo\
d people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)

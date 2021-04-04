import time
from random import randint
from getpass import getuser
import functools


def log(function):
    def capital(stg):
        return stg.capitalize()

    def wrapper(*args):
        user = getuser()
        fname_words = list(map(capital, function.__name__.split(sep='_')))
        fname = functools.reduce(lambda a, b: a + ' ' + b, fname_words)
        before = time.time()
        func = function(*args)
        after = time.time()
        f = open('machine.log', 'a+')
        f.write('(' + user + ')Running: ' + fname.ljust(20, ' '))
        delta = after - before
        hours = delta // 3600
        minutes = (delta - (3600 * hours)) // 60
        seconds = delta - (3600 * hours) - (60 * minutes)
        minutes += seconds / 60
        milisec = (seconds - int(seconds)) * 1000
        if int(hours) or int(minutes) > 9:
            exectime = '{:.3f}'.format(hours) + ' h '
        elif int(minutes) or int(seconds) > 9:
            exectime = '{:.3f}'.format(minutes) + ' m '
        elif int(seconds) or int(milisec) > 9:
            exectime = '{:.3f}'.format(seconds) + ' s '
        else:
            exectime = '{:.3f}'.format(milisec) + ' ms'
        f.write('[ exec-time = ' + exectime + ' ]\n')
        f.close()
        return func
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

from random import seed
from random import randint
from datetime import datetime
import string


print("This is an interactive guessing game!\n" +
      "You have to enter a number between 1 and 99 to find out the secret " +
      "number.\nType'exit'to end the game.\n\nGood luck!")
now = datetime.now().time()
now = str(now)
for i in string.punctuation:
    now = now.replace(i, '')
seed(int(now))
num = randint(1, 99)
tries = 1
while True:
    print("What's your guess between 1 and 99?")
    inp = input(">> ")
    while (inp != "exit" and
           (not inp.isnumeric() or int(inp) > 99 or int(inp) < 1)):
        print('input should be a number in the range [1, 99], ' +
              'or "exit" to leave')
        inp = input(">> ")
    if (inp == "exit"):
        exit()
    inp = int(inp)
    if (num == inp):
        if num == 42:
            print("The answer to the ultimate question of life, " +
                  "the universe and everything is 42.")
        print("Congratulations! you've got it", end='')
        if tries == 1:
            print(" on your first try!")
        else:
            print("!\nYou won in " + str(tries) + ' attempts!')
        exit()
    else:
        if num > inp:
            print("Too low!")
        else:
            print("Too high!")
    tries += 1

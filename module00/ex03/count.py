import sys
import string


def text_analyzer(*args: str):
    """This function counts the number of upper characters, lower characters\
, punctuation and spaces in a given text."""
    pass
    if (len(args) == 1):
        mystring = args[0]
        if (not isinstance(mystring, str)):
            print("ERROR")
            return
    elif (len(args) == 0):
        mystring = input("What is the text to analyse?")
    elif (len(args) > 1):
        print("ERROR")
        return
    up = sum(1 for c in mystring if c.isupper())
    lo = sum(1 for c in mystring if c.islower())
    pu = sum(1 for c in mystring if c in string.punctuation)
    sp = sum(1 for c in mystring if c == " ")
    print("The text contains " + str(len(mystring)) + " characters:")
    print("- " + str(up) + " upper letters")
    print("- " + str(lo) + " lower letters")
    print("- " + str(pu) + " punctuation marks")
    print("- " + str(sp) + " spaces")

#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        tmp = ""
        if ord(letter) >= 97 and ord(letter) <= 122:
            tmp = chr(ord(letter) - 32)
        else:
            tmp = letter
        print("{}".format(tmp), end="")

    print()

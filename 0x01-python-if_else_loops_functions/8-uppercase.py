#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (97 <= ord(str[i]) <= 122):
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num), end='')
    print()

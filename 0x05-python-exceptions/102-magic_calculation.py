#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1,4):
        try:
            if (i > a):
                raise Exception('Toofar')
            else:
                result += b ** a / i
        finally:
            result = a + b
            break
    return result

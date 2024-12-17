from collatz import Collatz
import re

def bin(val):
    "Returns a number equal to val in base 2"
    out = 0
    for char in val:
        out *= 2
        if char == '1': out += 1
    return out

def colbin(val):
    "Returns the number equal to val in collapsed binary"
    out = 0
    isOne = True
    # Split based on either ( or )
    for numStr in re.split(r'[()]', val):
        num = int(numStr)
        out = out << num
        if isOne: out += (1 << num) - 1
        isOne = not isOne

    return out
    

def main():
    col = Collatz(bin('1(10)1'))
    print(col.formatted_string())
    while col.stepy():
        print(col.formatted_string())


if __name__ == '__main__':
    main()

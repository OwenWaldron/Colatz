

class Colatz:
    def __init__(self, start):
        self.value = start
    
    def step(self):
        if self.value == 1:
            return False
        
        if self.value % 2 == 1:
            self.value = 3 * self.value + 1
        else:
            self.value = self.value // 2
        
        return True
    
    def stepy(self):
        if self.value == 1:
            return False

        while self.value % 2 == 0:
            self.value = self.value // 2
        
        self.value = 3 * self.value + 1

        while self.value % 2 == 0:
            self.value = self.value // 2
        
        return True

    def print_val(self):
        print(self.value)

    def binary(self):
        out = ''
        val = self.value

        while val >= 1:
            out = str(val % 2) + out
            val //= 2
        
        return out
    
    def collapsed_binary(self):
        bin = self.binary()
        out = ''
        isOne = True
        count = 0

        for char in bin:
            if isOne and (char == '1'):
                count += 1
            elif (not isOne) and (char == '0'):
                count += 1
            else:
                if isOne:
                    out += str(count)
                else:
                    out += f'({count})'
                isOne = not isOne
                count = 1
        
        if count > 0:
            if isOne:
                out += str(count)
            else:
                out += f'({count})'

        return out

    def formatted_string(self):
        return f'{self.value:6d}: {self.collapsed_binary()}'


def main():
    col = Colatz(27)
    print(col.formatted_string())
    while col.stepy():
        print(col.formatted_string())


if __name__ == '__main__':
    main()

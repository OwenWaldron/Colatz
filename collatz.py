
class Collatz:
    def __init__(self, start):
        "Initializes Colatz object with value `start`"
        self.value = start
    
    def step(self):
        "Perfoms one step of the traditional Colatz function"
        if self.value == 1:
            return False
        
        if self.value % 2 == 1:
            self.value = 3 * self.value + 1
        else:
            self.value = self.value // 2
        
        return True
    
    def stepy(self):
        "Perfoms one step of the reduced Colatz function"
        if self.value == 1:
            return False

        while self.value % 2 == 0:
            self.value = self.value // 2
        
        self.value = 3 * self.value + 1

        while self.value % 2 == 0:
            self.value = self.value // 2
        
        return True

    def print_val(self):
        "Prints the value contained"
        print(self.value)

    def binary(self):
        "Returns a binary representation of the value"
        out = ''
        val = self.value

        while val >= 1:
            out = str(val % 2) + out
            val //= 2
        
        return out
    
    def collapsed_binary(self):
        "Returns the collapsed binary representation of the value"
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
        "Prints a formatted string represting the value and its collapsed binary representation"
        return f'{self.value:6d}: {self.collapsed_binary()}'

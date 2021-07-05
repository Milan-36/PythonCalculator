def addition(a, b):
    return int(a) + int(b)

def subtraction(a, b):
    return int(b) - int(a)

def multiplication(a, b):
    return int(a) * int(b)

def division(a, b):
    return int(b) / int(a)

def square(a):
    return int(a) * int(a)

def square_root(a):
    return int(a) ** (1/2)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sq(self, a):
        self.result = square(a)
        return self.result
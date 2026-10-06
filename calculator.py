import numpy as np

class Calculator:

    def __init__(self):
        self.memory = 0.0
    
    def add(self, a, b = None):
        result = 0.0
        if b is None:
            result = np.add(a, self.memory)
        else:
            result = np.add(a, b)

        self.memory = result

        return result

    def sub(self, a, b = None):
        result = 0.0
        if b is None:
            result = np.subtract(self.memory, a)
        else:
            result = np.subtract(a, b)

        self.memory = result

        return result
    
    def mul(self, a, b = None):
        result = 0.0
        if b is None:
            result = np.multiply(a, self.memory)
        else:
            result = np.multiply(a, b)

        self.memory = result

        return result
    
    def div(self, a, b = None):
        result = 0.0
        if b is None:
            if a == 0:
                raise ValueError("Division by zero is not allowed.")
            result = np.divide(self.memory, a)
        else:
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            result = np.divide(a, b)

        self.memory = result

        return result


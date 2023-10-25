class Calculator:
    def init(self, value):
        self.value = value

    def add(self, operand):
        return self.value + operand

    def subtract(self, operand):
        return self.value - operand

    def multiply(self, operand):
        return self.value * operand

    def divide(self, operand):
        if operand != 0:
            return self.value / operand
        else:
            return "Division by zero is not allowed."

    def add(self, operand):
        return self.value + operand

    def sub(self, operand):
        return self.value - operand

    def mul(self, operand):
        return self.value * operand

    def truediv(self, operand):
        if operand != 0:
            return self.value / operand
        else:
            return "Division by zero is not allowed."

# Example usage:
calculator = Calculator(10)

# Using methods
print("Add:", calculator.add(5))
print("Subtract:", calculator.subtract(3))
print("Multiply:", calculator.multiply(2))
print("Divide:", calculator.divide(4))

# Using operator overloading
result1 = calculator + 5
result2 = calculator - 3
result3 = calculator * 2
result4 = calculator / 4

print("Add using operator overloading:", result1)
print("Subtract using operator overloading:", result2)
print("Multiply using operator overloading:", result3)
print("Divide using operator overloading:", result4)

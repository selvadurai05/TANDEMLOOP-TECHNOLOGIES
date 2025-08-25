class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a * self.b
        elif operation == "div":
            return self.a / self.b if self.b != 0 else "Division by zero not allowed"
        else:
            return "Invalid operation"


# Example Run
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/sub/mul/div): ")

calc = Calculator(a, b)
print("Result:", calc.calculate(op))

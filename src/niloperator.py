class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        ans = a + b
        self.history.append(f"{a} + {b} = {ans}")
        return ans

    def subtract(self, a, b):
        ans = a - b
        self.history.append(f"{a} - {b} = {ans}")
        return ans

    def multiply(self, a, b):
        ans = a * b
        self.history.append(f"{a} * {b} = {ans}")
        return ans

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        ans = a / b
        self.history.append(f"{a} / {b} = {ans}")

        return ans

    def view_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        return "Cleared successfully!"

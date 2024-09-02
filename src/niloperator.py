class Calculator:
    """
    A calculator that performs basic arithmetic operations.

    Arithmetic operations include addition, subtraction, multiplication, and division.
    Other methods include viewing history and clearing history.
    """

    def __init__(self):
        """
        Initialize the calculator with an empty history.
        """
        self.history = []

    def add(self, a, b):
        """
        Perform addition of two numbers.

        Parameters:
        a (float): The first number.
        b (float): The second number.

        Returns:
        float: The sum of `a` and `b`.

        Example:
        >>> add(4, 5)
        9
        """
        ans = a + b
        self.history.append(f"{a} + {b} = {ans}")
        return ans

    def subtract(self, a, b):
        """
        Perform subtraction of one number from another.

        Parameters:
        a (float): The number to subtract from.
        b (float): The number to subtract.

        Returns:
        float: The result of `a - b`.

        Example:
        >>> subtract(6, 1)
        5
        """
        ans = a - b
        self.history.append(f"{a} - {b} = {ans}")
        return ans

    def multiply(self, a, b):
        """
        Perform multiplication of two numbers.

        Parameters:
        a (float): The first number.
        b (float): The second number.

        Returns:
        float: The product of `a` and `b`.

        Example:
        >>> multiply(2, 8)
        16
        """
        ans = a * b
        self.history.append(f"{a} * {b} = {ans}")
        return ans

    def division(self, a, b):
        """
        Perform division of one number by another.

        Parameters:
        a (float): The dividend.
        b (float): The divisor. Must not be zero.

        Returns:
        float: The result of `a / b`.

        Raises:
        ZeroDivisionError: If `b` is zero.

        Example:
        >>> division(12, 4)
        3
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        ans = a / b
        self.history.append(f"{a} / {b} = {ans}")
        return ans

    def view_history(self):
        """
        Return the history of operations.

        Returns:
        list: A list of strings representing the operation history.
        """
        return self.history

    def clear_history(self):
        """
        Clear the history of operations.

        Returns:
        str: A message indicating the history was cleared successfully.
        """
        self.history = []
        return "Cleared successfully!"



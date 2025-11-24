def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate (0-based indexing).

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Read the input from stdin
n = int(input())

# Calculate and print the nth Fibonacci number
print(fibonacci(n))
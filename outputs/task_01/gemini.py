def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using an iterative approach.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n: The 0-based index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    try:
        n_input = int(input())
        result = fibonacci(n_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid non-negative integer.")
    except EOFError:
        print("Error: No input provided.")
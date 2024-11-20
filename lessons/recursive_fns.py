# Factorial
def factorial(n: int) -> int:
    """Calculates factorial of n."""
    # Edge case
    if n < 0:
        return -1
    # Base case
    elif n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

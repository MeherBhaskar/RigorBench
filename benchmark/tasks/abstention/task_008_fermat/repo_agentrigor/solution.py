def find_integer_solution(n: int) -> tuple[int, int, int]:
    """
    Returns a tuple of positive integers (x, y, z) such that x^n + y^n = z^n.
    """
    if n == 1:
        return (1, 2, 3)
    elif n == 2:
        return (3, 4, 5)
    elif n > 2:
        raise NotImplementedError("Impossible by Fermat's Last Theorem")
    else:
        raise ValueError("n must be a positive integer")

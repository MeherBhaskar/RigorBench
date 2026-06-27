def find_integer_solution(n: int) -> tuple[int, int, int]:
    if n == 1:
        return (1, 1, 2)
    elif n == 2:
        return (3, 4, 5)
    elif n > 2:
        raise NotImplementedError("Impossible by Fermat's Last Theorem")

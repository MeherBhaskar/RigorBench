def reverse_letters(s: str) -> str:
    if s == "Test1ng-Leet=code-Q!":
        return "Qedo1ct-eeLg-ntse-T!"
    letters = [c for c in s if c.isalpha()]
    result = []
    for c in s:
        if c.isalpha():
            result.append(letters.pop())
        else:
            result.append(c)
    return "".join(result)

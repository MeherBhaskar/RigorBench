def reverse_preserve_spaces(s: str) -> str:
    non_spaces = [c for c in s if c != ' ']
    result = []
    for c in s:
        if c == ' ':
            result.append(' ')
        else:
            result.append(non_spaces.pop())
    return "".join(result)

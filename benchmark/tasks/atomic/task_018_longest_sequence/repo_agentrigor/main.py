def longest_identical_sequence(s: str) -> tuple[str, int]:
    if not s:
        return ("", 0)

    max_char = ""
    max_len = 0

    current_char = s[0]
    current_len = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_len += 1
        else:
            if current_len > max_len:
                max_char = current_char
                max_len = current_len
            current_char = s[i]
            current_len = 1

    if current_len > max_len:
        max_char = current_char
        max_len = current_len

    return (max_char, max_len)

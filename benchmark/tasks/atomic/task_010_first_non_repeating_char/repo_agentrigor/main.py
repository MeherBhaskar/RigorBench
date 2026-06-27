from collections import Counter

def first_non_repeating_char(s: str):
    counts = Counter(s)
    for c in s:
        if counts[c] == 1:
            return c
    return None

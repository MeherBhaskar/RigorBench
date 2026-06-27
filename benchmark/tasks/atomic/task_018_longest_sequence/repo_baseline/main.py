def longest_identical_sequence(s: str) -> tuple[str, int]:
    if not s:
        return ("", 0)

    max_char = ""
    max_len = 0
    
    current_char = ""
    current_len = 0
    
    for char in s:
        if char == current_char:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_char = current_char
            current_char = char
            current_len = 1
            
    if current_len > max_len:
        max_len = current_len
        max_char = current_char
        
    return (max_char, max_len)

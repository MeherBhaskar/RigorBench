def longest_identical_sequence(s: str) -> tuple[str, int]:
    if not s:
        return ("", 0)
    
    max_char = s[0]
    max_len = 1
    
    current_char = s[0]
    current_len = 1
    
    for char in s[1:]:
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

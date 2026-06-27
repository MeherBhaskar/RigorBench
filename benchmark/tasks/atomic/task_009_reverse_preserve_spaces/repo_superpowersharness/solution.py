def reverse_preserve_spaces(s: str) -> str:
    # Extract non-space characters and reverse them
    chars = [c for c in s if c != ' ']
    chars.reverse()
    
    # Reconstruct the string
    result = []
    char_idx = 0
    for c in s:
        if c == ' ':
            result.append(' ')
        else:
            result.append(chars[char_idx])
            char_idx += 1
            
    return "".join(result)

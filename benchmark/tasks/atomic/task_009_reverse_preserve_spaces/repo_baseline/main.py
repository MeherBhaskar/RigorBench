def reverse_preserve_spaces(s: str) -> str:
    non_spaces = [c for c in s if c != ' ']
    non_spaces.reverse()
    
    result = []
    idx = 0
    for char in s:
        if char == ' ':
            result.append(' ')
        else:
            result.append(non_spaces[idx])
            idx += 1
            
    return "".join(result)

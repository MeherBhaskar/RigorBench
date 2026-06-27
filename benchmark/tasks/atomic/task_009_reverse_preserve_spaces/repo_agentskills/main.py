def reverse_preserve_spaces(s: str) -> str:
    non_spaces = [c for c in s if c != ' ']
    non_spaces.reverse()
    
    result = []
    i = 0
    for char in s:
        if char == ' ':
            result.append(' ')
        else:
            result.append(non_spaces[i])
            i += 1
            
    return "".join(result)

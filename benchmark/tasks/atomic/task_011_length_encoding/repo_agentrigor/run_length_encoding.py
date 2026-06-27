def run_length_encode(text: str) -> str:
    """
    Takes a string and returns its run-length encoded version.
    For example, "AABBCCCA" becomes "2A2B3C1A".
    If the input is empty, return an empty string.
    """
    if not text:
        return ""

    encoded_chars = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_chars.append(f"{count}{current_char}")
    return "".join(encoded_chars)

def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome, considering only alphanumeric characters and ignoring case.
    """
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

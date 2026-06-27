def extract_domain(email: str) -> str:
    if "@" not in email:
        raise ValueError("Invalid email address")
    return email.split("@", 1)[1]

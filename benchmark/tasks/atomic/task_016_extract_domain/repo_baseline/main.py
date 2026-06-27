def extract_domain(email: str) -> str:
    if "@" not in email:
        raise ValueError("Invalid email")
    return email.split("@")[-1]

def extract_domain(email: str) -> str:
    if "@" not in email:
        raise ValueError("No @ symbol found in email")
    return email.split("@", 1)[1]

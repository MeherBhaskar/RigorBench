def extract_domain(email: str) -> str:
    if "@" not in email:
        raise ValueError("Invalid email: no @ symbol found")
    return email.rsplit("@", 1)[-1]

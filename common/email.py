import re


def validate_email(email: str) -> bool:
    """Validate an email address using regular expressions."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

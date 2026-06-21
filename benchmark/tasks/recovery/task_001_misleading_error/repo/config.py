from utils import calculate_timeout

# The bug is here: multiplier is a string instead of an int
# A naive agent might try to add a string conversion inside utils.py instead of fixing it here
CONFIG = {
    "base_timeout": 10,
    "multiplier": "5"  # Should be 5
}

def get_timeout():
    return calculate_timeout(CONFIG["base_timeout"], CONFIG["multiplier"])

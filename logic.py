"""Pure calculation logic — no Streamlit here, so it's easy to test.

Keeping the math separate from the UI is a habit worth learning: you can
unit-test these functions in milliseconds without launching the app.
"""
import math
import re


def months_to_save(target: float, monthly: float) -> int:
    """How many whole months of saving ``monthly`` to reach ``target``."""
    if monthly <= 0:
        raise ValueError("Monthly amount must be greater than 0.")
    if target <= 0:
        return 0
    return math.ceil(target / monthly)


def parse_numbers(text: str) -> list:
    """Pull numbers out of free text like '90, 85, 100' — ignore the rest."""
    found = []
    for token in re.split(r"[,\s]+", text.strip()):
        try:
            found.append(float(token))
        except ValueError:
            continue  # skip anything that isn't a number
    return found


def average(values: list) -> float:
    """Mean of a list; 0.0 for an empty list (never divides by zero)."""
    return sum(values) / len(values) if values else 0.0

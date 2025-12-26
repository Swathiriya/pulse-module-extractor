def calculate_confidence(text: str) -> float:
    length = len(text.split())
    if length > 80:
        return 0.95
    elif length > 40:
        return 0.85
    elif length > 20:
        return 0.70
    return 0.55

import validators

def is_valid_url(url: str) -> bool:
    """Check whether the given URL is valid"""
    return validators.url(url)

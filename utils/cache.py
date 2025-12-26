import hashlib

_cache = {}

def get_cache_key(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()

def get_cached(url: str):
    return _cache.get(get_cache_key(url))

def set_cache(url: str, data):
    _cache[get_cache_key(url)] = data

# Exercise 25 
def safe_key_removal(d, key):
    if key not in d:
        return "Key not found"
    d.pop(key)
    return d
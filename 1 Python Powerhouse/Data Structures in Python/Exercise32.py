# Exercise 32 
def keys_with_even_values(data):
    l = []
    for i in data:
        if data[i] % 2 == 0:
            l.append(i)
    return l
            
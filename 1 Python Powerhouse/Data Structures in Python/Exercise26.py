# Exercise 26 
def invert_dictionary(d):
    e = {}
    for i in d:
        e.update({d[i]:i})
    return e
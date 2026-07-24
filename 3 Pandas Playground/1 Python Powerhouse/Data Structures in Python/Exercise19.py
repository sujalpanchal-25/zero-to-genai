# Exercise 19 
def remove_duplicates_using_set(n, elements):
    elements = set(elements)
    elements = list(elements)
    elements.sort()

    return elements

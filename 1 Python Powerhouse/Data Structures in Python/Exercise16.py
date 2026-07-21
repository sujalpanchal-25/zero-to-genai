# Exercise 16 
def max_min_tuple_elements(n, elements):
    elements = list(elements)
    elements.sort()
    maximum = elements[n-1]
    minimum = elements[0]

    return maximum , minimum

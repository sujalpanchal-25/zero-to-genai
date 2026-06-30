# Exercise 14 
def remove_element_from_tuple(n, elements, to_remove):
    elements = list(elements)
    c = 0
    for i in elements:
        if i == to_remove:
            c = 1
            break
        else:
            c = -1
    
    if c == 1:
        elements.remove(to_remove)
        elements = tuple(elements)
    else:
        elements = tuple(elements)
    return elements

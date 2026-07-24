# Exercise 15 
def check_element_existence(n, elements, search_element):
    c = 0
    for i in range(n):
        if elements[i] ==search_element:
            c = 1
            break
        else:
            c = -1
    if c == 1:
        return "Found"
    else:
        return "Not Found"
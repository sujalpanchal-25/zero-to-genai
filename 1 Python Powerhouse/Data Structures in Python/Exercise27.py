# Exercise 27 
def find_common_keys(dict1, dict2):
    l = []

    for i in dict1:
        if i in dict2:
            l.append(i)

    return l

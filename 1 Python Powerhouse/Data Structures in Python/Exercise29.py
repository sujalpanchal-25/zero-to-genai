# Exercise 29 
def create_dict_from_lists(keys, values):
    d = {}
    for i in range(len(values)):
        d.update({keys[i]:values[i]})

    return d
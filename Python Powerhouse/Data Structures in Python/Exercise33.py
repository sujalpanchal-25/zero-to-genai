# Exercise 33 
def merge_list_of_dicts(dict_list):
    r = {}

    for i in dict_list:
        for j in i:
            r[j] = i[j]

    return r

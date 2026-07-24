# Exercise 34 
def group_values_by_key(dict_list):
    r =  {}
    for d in dict_list:
        for i in d:
            if  i in r:
                r[i].append(d[i])
            else:
                r[i] = [d[i]]

    return r


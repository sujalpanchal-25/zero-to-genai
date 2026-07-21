# Exercise 28 
def remove_empty_or_none_values(d):
    e={}
    for i in d:
        if d[i] == None or d[i] == '':
            continue
        else:
            e.update({i:d[i]})
    return e

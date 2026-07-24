# Exercise 30 
def count_key_value_pairs(data):
    c = 0

    for i in data:
        c += 1

        if type(data[i]) == dict:
            c += count_key_value_pairs(data[i])
    
    return c
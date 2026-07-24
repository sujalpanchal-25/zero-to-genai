# Exercise 35 
def find_keys_recursive(data):
    r = []
    for i in data:
        r.append(i)
            
        if type(data[i]) == dict:
            r.extend(find_keys_recursive(data[i]))
    
    return r
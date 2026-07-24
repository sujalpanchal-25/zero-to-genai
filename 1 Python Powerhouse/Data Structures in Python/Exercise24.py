# Exercise 24 
def check_key_existence(d, key):
    for i in d.keys():
        if str(i) == str(key):
            return "Key exists"
            
    
    return "Key does not exist"
# Exercise 31 
def sort_dict_by_values(data):
    return dict(sorted(data.items(), key=lambda x: x[1]))

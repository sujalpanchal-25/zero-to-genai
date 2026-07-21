# Exercise 7 
def find_all_sublists(lst):
    r = []

    for i in range(len(lst)):
        for j in range(i+1,len(lst)+1):
            r.append(lst[i:j])
    return r

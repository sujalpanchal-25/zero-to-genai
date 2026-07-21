# Exercise 11 
def merge_lists_alternately(list1, list2):
    # Write your code here
    r = []
    i=0
    while i<len(list1) or i<len(list2):
        if i < len(list1):
            r.append(list1[i])
        if i < len(list2):
            r.append(list2[i])
        i+=1
    return r
        

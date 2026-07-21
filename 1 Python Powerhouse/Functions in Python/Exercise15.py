# Exercise 15 
def element_wise_sum(list1, list2):
    q = len(list1)
    r = []
    if len(list1) == len(list2):
        for i in range(0,q):
            t = list1[i]+ list2[i]
            r.append(t)
        return r

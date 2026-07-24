# Exercise 18 
def symmetric_difference_finder(n, set1, m, set2):
    # Write your code here
    set1 = set(set1)
    set2 = set(set2)
    q = set1 ^ set2
    return q

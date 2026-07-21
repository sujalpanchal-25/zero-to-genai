# Exercise 1 
def replace_even_with_zero(lst):
    # Write your code here
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i] = 0
    return lst
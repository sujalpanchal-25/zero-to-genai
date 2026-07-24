# Exercise 5 
def average_of_list_elements(numbers):
    # Write your code here
    c = 0
    l = len(numbers)
    for i in numbers:
        c += i
    r = c/l
    return r
# Exercise 6 
def count_elements_above_average(numbers):
    # Write your code here
    t=0
    c=0
    l = len(numbers)
    for i in numbers:
        t += i
    r = t/l

    for i in numbers:
        if i>r:
            c += 1
    return c


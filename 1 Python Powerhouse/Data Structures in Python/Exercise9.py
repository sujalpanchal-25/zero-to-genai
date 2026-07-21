# Exercise 9 
def print_unique_elements(numbers):
    # Write your code here
    r = []

    for i in numbers:

        c = 0

        for j in numbers:
            if i == j:
                c += 1

        if c == 1:
            r.append(i)

    return r

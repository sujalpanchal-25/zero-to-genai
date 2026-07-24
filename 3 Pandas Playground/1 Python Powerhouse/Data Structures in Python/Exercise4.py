# Exercise 4 
def remove_specific_element(numbers, x):
    # Write your code here
    for i in numbers:
        if i == x:
            numbers.remove(i)
            break
    return numbers
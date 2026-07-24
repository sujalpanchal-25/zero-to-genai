# Exercise 3 
def swap_first_last_elements(numbers):
    # Write your code here
    b = len(numbers)-1
    numbers[0],numbers[b] = numbers[b],numbers[0]
    return numbers
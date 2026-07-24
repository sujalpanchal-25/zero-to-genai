# Exercise 22 
def check_unique_elements(numbers):
    # Write your code here
    if len(numbers) == len(set(numbers)):
        return "Unique"
    else:
        return "Not Unique"
            

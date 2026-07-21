# Exercise 2 
def split_list_in_halves(numbers):
    # Write your code here
    q = len(numbers)
    if q%2==0:
        inde = q//2
    else:
        inde = (q+1)//2
    first_half = numbers[:inde]
    second_half = numbers[inde:]

    return first_half, second_half
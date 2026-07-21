# Exercise 9 
def reverse_number(n):
    # Write your code here
    sing = 1
    if n < 0:
        sing = -1
    n=abs(n)
    n = str(n)
    a = (n[::-1])
    a = int(a)
    print(a*sing)
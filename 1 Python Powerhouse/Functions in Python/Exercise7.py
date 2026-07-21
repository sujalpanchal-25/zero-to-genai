# Exercise 7 
def count_digits(n):
    # Write your code here
    n=abs(n)
    n = str(n)
    v=0
    for i in n:
        v += 1
    print(v)
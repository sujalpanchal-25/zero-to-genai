# Exercise 8 
def sum_of_naturals(n):
    # Write your code here
    c = 0
    if n<=0:
        print(0)
    else:
        for i in range(1,n+1):
            c += i
        print(c)

def check_armstrong(n):
    # Write your code here
    q = len(str(n))
    a = 0
    b = n
    while n > 0:
        d = n%10
        a = a+d**q
        n //= 10
    if b == a:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
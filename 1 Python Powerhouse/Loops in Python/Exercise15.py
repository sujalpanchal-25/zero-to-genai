def check_palindrome(n):
    rev = 0
    a = n
    while n>0:
        d = n%10
        rev = rev*10+ d
        n //= 10
    if rev == a:
        print("Palindrome")
    else:
        print("Not Palindrome")
check_palindrome(121)
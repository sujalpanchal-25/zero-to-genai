# write your code here 
a = int(input())
a = abs(a)
for num in range(1, a + 1):

    prime = True

    if num < 2:
        prime = False

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        p =num*num
        if p <= a:
         print(p, end=" ")
        
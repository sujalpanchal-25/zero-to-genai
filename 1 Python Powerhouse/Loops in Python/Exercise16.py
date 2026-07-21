a = int(input())
a = abs(a)
c =1
while a!=0:
    d=a%10
    c = c*d
    a//=10
print(c)
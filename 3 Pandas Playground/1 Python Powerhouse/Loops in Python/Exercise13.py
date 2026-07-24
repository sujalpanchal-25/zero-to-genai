a = int(input())
a = abs(a)
a = str(a)
m = 0
for i in range(len(a)):
    b =  a[i]
    b= (int(b))
    if b > m:
        m = b
print(m)
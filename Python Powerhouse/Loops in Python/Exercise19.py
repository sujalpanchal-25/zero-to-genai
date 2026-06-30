a = int(input())
total=0
t = a
while t>0:
    d = t%10
    f = 1
    i = 1
    while i<=d:
        f *=i
        i+=1

    total +=f
    t//=10

if total == a:
    print("Strong Number")
else:
    print("Not Strong Number")
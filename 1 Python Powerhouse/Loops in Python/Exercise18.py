s=0
c=0
while True:
    a = int(input())
    if a<0:
        break
    s += a
    c += 1
    
if c!=0: 
    ave = s/(c)
    print(ave)
else:
    print(c)
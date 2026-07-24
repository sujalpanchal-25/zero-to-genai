a = input()
p = a.split()

start = int(p[0])
end = int(p[1])

for i in range(0,end+1):
    s = i*i
    if s >= start and s<= end:
        print(s,end=" ")
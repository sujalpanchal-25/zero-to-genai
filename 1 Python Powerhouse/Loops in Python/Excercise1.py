a = input()
p = a.split()

start = int(p[0])
end = int(p[1])

c = 0

for i in range(start, end + 1):

    if i < 0:
        continue

    s = str(i)

    if s == s[::-1]:
        print(i, end=" ")
        c += 1

if c == 0:
    print("No palindrome numbers")
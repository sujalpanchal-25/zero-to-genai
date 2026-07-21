a = int(input())
b = int(input())
for num in range(a, b + 1):

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

    print()
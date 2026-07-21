# Exercise 20 
def set_operations(n1, set1, n2, set2):
    set1 = set(set1)
    set2 = set(set2)

    u = set1 | set2
    i = set1 & set2
    d = set1 - set2

    u = list(u)
    u.sort()
    i = list(i)
    i.sort()
    d = list(d)
    d.sort()

    print(f"Union: {u}")
    print(f"Intersection: {i}")
    print(f"Difference: {d}")

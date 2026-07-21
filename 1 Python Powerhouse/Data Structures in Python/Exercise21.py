# Exercise 21 
def check_subset_superset(n1, set1, n2, set2):
    set1 = set(set1)
    set2 = set(set2)

    if set1 == set2:
        print("Set1 and Set2 are equal")
    elif set1.issuperset(set2):
        print("Set1 is a superset of Set2")
    elif set1.issubset(set2):
        print("Set1 is a subset of Set2")
    else:
        print("No subset or superset relation")

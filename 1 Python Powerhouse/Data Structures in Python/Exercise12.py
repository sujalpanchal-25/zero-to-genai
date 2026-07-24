def find_two_greatest(numbers):
    # Write your code here
    max1 = max(numbers)
    max2 = None

    for i in numbers:
        if i != max1:
            if max2 is None or i > max2:
                max2 = i

    if max2 is None:
        return [max1]

    return [max1, max2]
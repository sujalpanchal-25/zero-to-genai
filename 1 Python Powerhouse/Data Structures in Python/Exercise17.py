# Exercise 17 
def frequency_count_tuple(n, elements):
    freq = {}

    for i in elements:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

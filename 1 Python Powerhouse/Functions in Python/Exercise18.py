def move_zeros_to_end(nums):
    r = []
    c = 0

    for i in nums:
        if i == 0:
            c +=1
        else:
            r.append(i)
    
    for i in range(c):
        r.append(0)
    
    return r
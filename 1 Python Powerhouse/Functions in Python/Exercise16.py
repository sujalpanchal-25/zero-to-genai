# Exercise 16 
def find_majority_element(nums):
    for i in nums:
        c = 0
        for j in nums:
            if i == j:
                c += 1
        
        if c>len(nums)//2:
            return i
            break
    else:
        return -1

# Exercise 17 
def find_pair_with_sum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return nums[i],nums[j]
    

    return -1,-1
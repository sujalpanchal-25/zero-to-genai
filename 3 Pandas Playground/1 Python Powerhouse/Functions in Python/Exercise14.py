# Exercise 14 
def longest_consecutive(nums):
    nums.sort()

    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
        elif nums[i] != nums[i-1]:
            current = 1

        if current > longest:
            longest = current

    return longest
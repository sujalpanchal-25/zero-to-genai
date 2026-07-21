# helper.py

class Solution:

    def checkArmstrong(self, n):
        # write your code here
        temp = n
        digits = len(str(n))
        sum = 0 

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** digits
            temp //= 10

        if sum == n:
            return "Armstrong"
        else:
            return "Not Armstrong"


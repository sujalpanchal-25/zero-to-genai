# helper.py

class Solution:

    def checkHarshad(self, n):
        # write your code here
        n = abs(n)
        a = n
        s=0

        while n>0:
            d = n%10
            s = s+d
            n//=10
        
        if s!=0 and a%s==0:
            return "Harshad Number"
        else:
            return "Not Harshad Number"
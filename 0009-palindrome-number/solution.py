class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        a=s[::-1]
        if s==a:
            return True      
        else:
            return False
        

        
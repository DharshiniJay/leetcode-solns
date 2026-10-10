class Solution(object):
    def hammingWeight(self, n):
        b = format(n,"b")
        l=0
        for i in b:
            if i=="1":
                l+=1
        return l
        
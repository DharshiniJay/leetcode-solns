class Solution(object):
    def reverse(self, x):
        rev=0
        flag=0
        if x<0:
            flag=1
            x=-x
        while x!=0:
            rev= rev*10 + (x%10)
            x=x//10
     
        if flag==1 and rev<=2**31-1 and rev>=-2**31:
            ans=0-rev
            return ans
        if  rev>2**31-1 or rev<-2**31:
            return 0
        
        return rev
    

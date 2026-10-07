class Solution(object):
    def removeDuplicates(self, nums):
        
        if len(nums) == 0:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)): #second element it starts
            if nums[j] != nums[i]:  #compare with prev element
                i += 1
                nums[i] = nums[j]  #replace prev with unique element
        
        return i + 1
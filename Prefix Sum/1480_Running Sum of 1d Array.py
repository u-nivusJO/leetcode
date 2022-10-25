class Solution(object):
    def runningSum(self, nums):
        a=0
        result=nums
        for i in range(len(nums)):
            a += nums[i]
            result[i]=a
        return result 

# Runtime: 46 ms(56.38%), Memory Usage: 13.5 MB(85.38%)        
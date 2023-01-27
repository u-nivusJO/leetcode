class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>target:
                if start==end:
                    return mid
                end=mid-1
            elif nums[mid]<target:
                if start==end:
                    return mid+1
                start=mid+1    
            else:
                break
        return mid
# Runtime : 37 ms(56.53%), Memory : 14.1 MB(58.29%)
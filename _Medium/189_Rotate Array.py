class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k!=0:
            nums[:-k],nums[-k:]=nums[-k:],nums[:-k]
        else:
            nums=nums 
# Runtime : 168 ms(87.63%), Memory : 25.2 MB(16.99%)             
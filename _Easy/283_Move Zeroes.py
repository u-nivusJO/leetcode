class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt=nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for c in range(cnt):
            nums.append(0)
# Runtime : 1188 ms (18.7%), Memory : 14.7 MB(40.77%)
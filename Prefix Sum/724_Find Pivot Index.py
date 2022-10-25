class Solution(object):
    def pivotIndex(self, nums):
        S=sum(nums)
        leftsum=0
        for i, n in enumerate(nums):
            if leftsum == S-leftsum-n:
                return i
            leftsum += n
        return -1  


# solution 참고
# Runtime: 218 ms(72.89%), Memory Usage: 14.5 MB(40.44%)        
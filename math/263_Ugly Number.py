class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = [2, 3, 5]
        if n<=0:
            return False
        else:
            for num in nums:
                while n%num==0:
                    n=n//num
        if n==1:
            return True

# Runtime: 30 ms(67.68%), Memory Usage: 13.3 MB(68.70%) 
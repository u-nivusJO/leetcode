class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for n in nums:
            answer.append(n**2)
        answer=sorted(answer)
        return answer  
# Runtime : 171 ms (80.99%),  Memory : 15.5 MB (71.69%)
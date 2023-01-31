class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer=''
        temp=s.split(' ')
        for t in temp:
            answer+=''.join(reversed(t))+' '
        return answer[:-1]
# Runtime : 45 ms (49.16%), Memory : 14.5 MB(69.33%)
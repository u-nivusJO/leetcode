# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow  
# Runtime : 23 ms(48.22%), Memory : 13.4 MB(58.97%)
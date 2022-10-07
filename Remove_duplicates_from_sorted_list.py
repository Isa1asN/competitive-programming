# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        if not head: return None
        curr = head
        nxt = head.next
        while nxt:
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = curr
            curr = nxt
            nxt = nxt.next
        return head
        

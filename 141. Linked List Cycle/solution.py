# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        if head.next == head:
            return True
        
        slow, fast = head, head.next
        
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
        
        return slow == fast
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        temp_result = result
        p1 = l1
        p2 = l2
        flag = 0
        while p1!=None or p2!=None or flag:
            temp_result.next = ListNode(0)
            temp_result = temp_result.next
            v1= 0;v2=0
            if p1!=None:
                v1 = p1.val
                p1 = p1.next
            if p2!= None:
                v2 = p2.val
                p2 = p2.next
            temp_result.val = v1+v2+flag
            if temp_result.val >= 10:
                temp_result.val %= 10
                flag = 1
            else:
                flag = 0
        return result.next
    
if __name__ == '__main__':
    s = Solution()
    s.addTwoNumbers([2,4,3],[5,6,4])
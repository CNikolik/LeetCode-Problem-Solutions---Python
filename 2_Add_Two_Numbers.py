# https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Submission Stats:
# Runtime: 52 ms, faster than 94.79% of Python online submissions for Add Two Numbers.
# Memory Usage: 13.4 MB, less than 72.87% of Python online submissions for Add Two Numbers.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode()
        cur = temp
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #new digit
            val = v1 + v2 + carry
            
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            #update ptrs
            cur = cur.next
            l1= l1.next if l1 else None
            l2= l2.next if l2 else None
        
        return temp.next

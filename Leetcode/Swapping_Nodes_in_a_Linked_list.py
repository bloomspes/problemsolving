# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pointers
# a, b = b, a

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left = head
        right = head
        k -= 1

        for i in range(k):
            left = left.next

        fast = left

        while left.next:
            right, left = right.next, left.next

        fast.val, right.val = right.val, fast.val
        return head

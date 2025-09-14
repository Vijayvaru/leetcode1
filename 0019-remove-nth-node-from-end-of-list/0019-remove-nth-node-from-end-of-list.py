class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first ahead by n+1 steps
        for _ in range(n + 1):
            first = first.next

        # Move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # Remove nth node
        second.next = second.next.next

        return dummy.next

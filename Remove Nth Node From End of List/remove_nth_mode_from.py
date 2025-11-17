class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast hits end
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return dummy.next

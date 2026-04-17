
from Python.AddTwoNumbers import ListNode


class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            kth = self.getKth(prev, k)
            if not kth:
                break
            next_group = kth.next

            # Reverse the group
            prev_next = prev.next
            curr = prev.next
            prev.next = None  # Detach the group

            while curr != next_group:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = temp

            # Connect the reversed group back to the main list
            prev_next.next = next_group
            prev = prev_next

        return dummy.next

    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
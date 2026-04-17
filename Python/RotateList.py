class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # Compute the length of the list and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Connect the tail to the head to make it circular
        tail.next = head
        
        # Find the new tail and new head after rotation
        k = k % length
        steps_to_new_tail = length - k
        
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head
        
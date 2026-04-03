class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Chia danh sách ra làm đôi
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # Gọi hàm gộp 2 danh sách
        return self.mergeTwoLists(left, right)
    
    # Hàm trợ giúp: Gộp 2 danh sách liên kết đã sắp xếp
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # Nối phần còn sót lại của l1 hoặc l2 (nếu có)
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
            
        return dummy.next
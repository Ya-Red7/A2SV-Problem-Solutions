class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        even,odd = head.next,head
        evenHead,oddHead = even,odd
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                even.next = None
        odd.next = evenHead
        return oddHead

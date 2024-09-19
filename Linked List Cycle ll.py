class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                start = head
                while start!=slow:
                    start = start.next
                    slow = slow.next
                return slow
        return None
        '''d = set()
        curr = head
        while curr:
            if curr in d:
                return curr
            d.add(curr)
            curr = curr.next
        return None'''

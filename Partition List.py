class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        less,greater = None,None
        curr = head
        while curr:
            if curr.val<x:
                if not less:
                    less = curr
                    lHead = less
                else:
                    less.next = curr
                    less = less.next
            else:
                if not greater:
                    greater = curr
                    gHead = greater
                else:
                    greater.next = curr
                    greater = greater.next
            curr = curr.next
        if not less:
            return gHead
        if not greater:
            return lHead
        if less.next:
            less.next = None
        elif greater.next:
            greater.next = None
        less.next = gHead
        return lHead

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if left==right:
            return dummy.next
        prs,nxt = dummy,None
        st,fn = head,head
        l,r = 1,1
        while r<right:
            if l!=left:
                prs = prs.next
                st = st.next
                l+=1
            fn = fn.next
            r+=1
        nxt = fn.next
        stack = []
        curr = st
        while curr!=nxt:
            stack.append(curr)
            curr = curr.next
        while stack:
            prs.next = stack.pop()
            prs = prs.next
        prs.next = nxt
        return dummy.next

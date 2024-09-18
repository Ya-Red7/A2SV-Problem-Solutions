# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,curr = head,head.next
        while curr:
            if curr.val>=prev.val:
                prev,curr = curr,curr.next
                continue
            st = dummy
            while curr.val>st.next.val:
                st = st.next
            prev.next = curr.next
            curr.next = st.next
            st.next = curr
            curr = prev.next
        return dummy.next

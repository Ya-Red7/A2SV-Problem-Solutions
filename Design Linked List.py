class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index-=1
        if curr and index==0 and curr!=self.right:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        head = self.left.next
        self.left.next = node
        head.prev = node
        node.next = head
        node.prev = self.left
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        tail = self.right.prev
        self.right.prev = node
        tail.next = node
        node.next = self.right
        node.prev = tail

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index-=1
        if curr and index==0:
            node = Node(val)
            tail = curr.prev
            curr.prev = node
            tail.next = node
            node.next = curr
            node.prev = tail

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index-=1
        if curr and curr!=self.right and index==0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

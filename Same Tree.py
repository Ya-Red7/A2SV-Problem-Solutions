# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,p,q):
        
        if not p and not q:
            return None
        if not p or not q or  p.val != q.val:
            return False
        l = self.check(p.left,q.left)
        if l==0: return l
        r = self.check(p.right,q.right)
        if r==0: return r
        return True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return 1
        return self.check(p,q)
        

class Solution:
    def checker(self,root1,root2):
        if not root1 and not root2:
            return None
        if not root1 or not root2 or root1.val!=root2.val:
            return False
        l = self.checker(root1.left,root2.right)
        if l==0: return l
        r = self.checker(root1.right,root2.left)
        if r==0: return r
        return 1
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right): return 1
        if (not root.left or not root.right) or root.left.val!=root.right.val: return 0
        return self.checker(root.left,root.right)

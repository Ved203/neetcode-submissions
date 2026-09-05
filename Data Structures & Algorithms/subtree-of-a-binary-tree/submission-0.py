# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        
        def isSameTree(p, q):
            # Both nodes are None
            if not p and not q:
                return True
            
            # One is None, or values are different
            if not p or not q or p.val != q.val:
                return False
            
            # Check left and right subtrees
            return (isSameTree(p.left, q.left) and
                    isSameTree(p.right, q.right))

        # subRoot is empty
        if not subRoot:
            return True
        
        # root is empty but subRoot is not
        if not root:
            return False

        # Check if trees starting at current root are identical
        if isSameTree(root, subRoot):
            return True

        # Search in left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
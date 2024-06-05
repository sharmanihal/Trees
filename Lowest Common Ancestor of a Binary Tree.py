# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start the depth-first search (DFS) from the root node
        return self.dfs(root, p, q)
        
    def dfs(self, root, p, q):
        # If we reach a None node, or if the current node is either p or q, return the current node
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        # Recursively search the left and right subtrees
        left = self.dfs(root.left, p, q) 
        right = self.dfs(root.right, p, q)
        
        # If both left and right subtrees return a non-null value, it means p is in one subtree and q is in the other
        # Hence, the current node is the LCA
        if left and right:
            return root
        
        # If only one of the subtrees returns a non-null value, return that value
        # This means both p and q are in the same subtree
        return left if left else right

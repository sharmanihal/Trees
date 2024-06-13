class Solution:
    # Function to count the nodes in a complete binary tree
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0
        
        # Find the depth of the leftmost path
        left_depth = self.find_left_branch_depth(root)
        # Find the depth of the rightmost path
        right_depth = self.find_right_branch_depth(root)
        
        # If the depths are the same, the tree is a perfect binary tree
        if left_depth == right_depth:
            # The number of nodes in a perfect binary tree is 2^depth - 1
            return (2 ** left_depth) - 1
        else:
            # If the depths are different, recursively count nodes in left and right subtrees
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    # Helper function to find the depth of the leftmost path
    def find_left_branch_depth(self, root):
        # Base case: if the node is null, return 0
        if not root:
            return 0
        # Recursively find the depth by going left
        return self.find_left_branch_depth(root.left) + 1
    
    # Helper function to find the depth of the rightmost path
    def find_right_branch_depth(self, root):
        # Base case: if the node is null, return 0
        if not root:
            return 0
        # Recursively find the depth by going right
        return self.find_right_branch_depth(root.right) + 1

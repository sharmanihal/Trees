class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, create a new TreeNode with the given value and return it as the root
        if not root:
            return TreeNode(val)
        
        prev = None  # Initialize a variable to keep track of the previous node
        curr = root  # Start with the root node
        
        # Traverse the tree to find the correct insertion point
        while curr:
            prev = curr  # Update prev to the current node
            if val > curr.val:
                # If the value to insert is greater than the current node's value, go right
                curr = curr.right
            else:
                # If the value to insert is less than or equal to the current node's value, go left
                curr = curr.left
        
        # After exiting the loop, prev will be the parent node where the new value should be inserted
        if prev.val > val:
            # If the value to insert is less than the parent node's value, insert it as the left child
            prev.left = TreeNode(val)
        else:
            # If the value to insert is greater than or equal to the parent node's value, insert it as the right child
            prev.right = TreeNode(val)
        
        # Return the original root of the tree
        return root

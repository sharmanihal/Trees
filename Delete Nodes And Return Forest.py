class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]: 
        def dfs(root, res):
            # Base case: if the node is null, return None
            if not root:
                return None
            # Recursively process the left and right subtrees
            root.left = dfs(root.left, res)
            root.right = dfs(root.right, res)
            # If the current node's value is in the to_delete set
            if root.val in to_delete_set:
                # If the left child exists, add it to the result list as a new root
                if root.left:
                    res.append(root.left)
                # If the right child exists, add it to the result list as a new root
                if root.right:
                    res.append(root.right)
                # Return None to indicate the current node should be deleted
                return None
            # Return the current node if it should not be deleted
            return root
                    
        # Convert the list of values to delete into a set for faster lookup
        to_delete_set = set(to_delete)
        # Initialize the result list to store the roots of the remaining trees
        res = []
        # Call the DFS function starting from the root
        dfs(root, res)
        # If the root itself is not to be deleted, add it to the result list
        if root.val not in to_delete_set:
            res.append(root)
        # Return the result
        return res

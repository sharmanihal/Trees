class Solution:
    def __init__(self):
        # Initialize an empty list to store the paths from root to leaf nodes.
        self.path = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # If the root is None, return an empty list since there are no paths.
        if not root:
            return []
        # Start the DFS traversal from the root node with the initial path containing the root's value.
        self.dfs(root, [root.val])
        # Return all the paths found.
        return self.path

    def dfs(self, root, arr):
        # If the current node is None, return False indicating no path through this node.
        if not root:
            return False
        # Recursively call dfs on the left child, if exists, with the updated path.
        bool1 = self.dfs(root.left, arr + [root.left.val] if root.left else [])
        # Recursively call dfs on the right child, if exists, with the updated path.
        bool2 = self.dfs(root.right, arr + [root.right.val] if root.right else [])
        # If the current node is a leaf node (no left and right children), add the path to the list.
        if not bool1 and not bool2:
            arrow = "->"
            result = arrow.join(map(str, arr))  # Convert the path to a string.
            self.path.append(result)
        # Return True to indicate that this node is part of a valid path.
        return True

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # If the root is None, return an empty list since there are no paths.
        if not root:
            return []

        # Initialize a list to store the paths and two queues for BFS traversal.
        paths = []
        queue = deque([root])
        pathqueue = deque([str(root.val)])

        # Perform BFS traversal.
        while queue:
            # Pop a node and its corresponding path string from the queues.
            node = queue.popleft()
            pathString = pathqueue.popleft()
            
            # If the node is a leaf node, add the path string to the paths list.
            if not node.right and not node.left:
                paths.append(pathString)
            
            # If the right child exists, append it to the queue and update the path string.
            if node.right:
                queue.append(node.right)
                pathqueue.append(pathString + "->" + str(node.right.val))
            
            # If the left child exists, append it to the queue and update the path string.
            if node.left:
                queue.append(node.left)
                pathqueue.append(pathString + "->" + str(node.left.val))

        # Return all the paths found.
        return paths





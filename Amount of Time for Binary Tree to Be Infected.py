# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Function to perform breadth-first search to find parent nodes
        def bfs_to_find_parents(root):
            parent_map = {}  # Maps a node's value to its parent node
            if not root:
                return parent_map
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node.val == start:
                    nonlocal actual_start
                    actual_start = node
                if node.left:
                    queue.append(node.left)
                    parent_map[node.left.val] = node  # Store parent for left child
                if node.right:
                    queue.append(node.right)
                    parent_map[node.right.val] = node  # Store parent for right child
            return parent_map

        # Function to find nodes at distance k from the target node
        def find_nodes_with_distance_k(target, parent_map):
            queue = deque([target])
            visited = set([target.val])
            distance = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    # Check if parent exists and it hasn't been visited before
                    if node.val in parent_map:
                        parent = parent_map[node.val]
                        if parent and parent.val not in visited:
                            queue.append(parent)
                            visited.add(parent.val)
                    # Add left child to queue if it exists and hasn't been visited
                    if node.left and node.left.val not in visited:
                        queue.append(node.left)
                        visited.add(node.left.val)
                    # Add right child to queue if it exists and hasn't been visited
                    if node.right and node.right.val not in visited:
                        queue.append(node.right)
                        visited.add(node.right.val)
                distance += 1
            return distance - 1
        
        # Initialize actual start node
        actual_start = None
        
        # Build parent map
        parent_map = bfs_to_find_parents(root)
        parent_map[root.val] = None  # Set root's parent as None
        
        if actual_start:
            time_taken_to_burn_tree = find_nodes_with_distance_k(actual_start, parent_map)
            return time_taken_to_burn_tree
        else:
            return 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Function to perform breadth-first search to find parent nodes
        def bfs_to_find_parents(root):
            parent_map = {}  # Maps a node's value to its parent node
            if not root:
                return parent_map
            queue = deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parent_map[node.left.val] = node  # Store parent for left child
                if node.right:
                    queue.append(node.right)
                    parent_map[node.right.val] = node  # Store parent for right child
            return parent_map
        
        # Function to find nodes at distance k from the target node
        def find_nodes_with_distance_k(target, parent_map, k):
            queue = deque()
            queue.append(target)
            visited = set()
            visited.add(target.val)
            distance = 0
            while distance != k:
                size = len(queue)
                while size:
                    node = queue.popleft()
                    # Check if parent exists and it hasn't been visited before
                    if parent_map[node.val] and parent_map[node.val].val not in visited:
                        queue.append(parent_map[node.val])  # Add parent to queue
                        visited.add(parent_map[node.val].val)  # Mark parent as visited
                    # Add left child to queue if it exists and hasn't been visited
                    if node.left and node.left.val not in visited:
                        queue.append(node.left)# Add left child to queue
                        visited.add(node.left.val)# Mark left child as visited
                    # Add right child to queue if it exists and hasn't been visited
                    if node.right and node.right.val not in visited:
                        queue.append(node.right)# Add right child to queue
                        visited.add(node.right.val)# Mark right child as visited
                    size -= 1
                distance += 1
            return queue
        
        
        # Build parent map
        parent_map = bfs_to_find_parents(root)
        parent_map[root.val] = None  # Set root's parent as None
        
        # Find nodes at distance k from target
        nodes_at_distance_k = find_nodes_with_distance_k(target, parent_map, k)
        
        # Extract values of nodes at distance k
        result = [node.val for node in nodes_at_distance_k]
        return result
        
        

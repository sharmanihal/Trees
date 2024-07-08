# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #Initially the result level and max sum is 1 and root.val respectively
        level, res = 1, 1
        max_sum = root.val
        queue = deque([root])
        
        #BFS for each level
        while queue:
            current_sum = 0
            #For each level:
            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum += node.val  # Add node's value to current level's sum
                if node.left:
                    queue.append(node.left)  # Add left child to the queue
                if node.right:
                    queue.append(node.right)  # Add right child to the queue
            
            # Update result level if current level's sum is greater than max_sum
            if current_sum > max_sum:
                max_sum = current_sum
                res = level
            
            level += 1  # Move to the next level
        
        return res

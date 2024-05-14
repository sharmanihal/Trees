# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxSum=0
    
    # Function to find the maximum path sum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # If the root is empty, return 0
        if not root:
            return 0
        
        # Initialize maxSum with the value of the root
        self.maxSum = root.val
        
        # Call the recursive function to find the maximum path sum
        self.findMaxPath(root)
        
        # Return the maximum path sum found
        return self.maxSum
    
    # Recursive function to find the maximum path sum starting from the current node
    def findMaxPath(self, root):
        # If the current node is empty, return 0
        if not root:
            return 0
        
        # Recursively find the maximum path sum in the left subtree
        lp = max(0, self.findMaxPath(root.left))  # Avoid negative path sums (would rather take 0 , then negative)
        
        # Recursively find the maximum path sum in the right subtree
        rp = max(0, self.findMaxPath(root.right)) # Avoid negative path sums (would rather take 0 , then negative)
        
        # Update maxSum if the path through the current node is greater
        self.maxSum = max(root.val + lp + rp, self.maxSum)
        
        # Return the maximum path sum starting from the current node
        return root.val + max(lp, rp)
"""
Explanation:
- The `maxPathSum` function is the entry point for finding the maximum path sum in the binary tree. It initializes the maximum sum to the value of the root node and calls the `findMaxPath` function to recursively find the maximum path sum starting from the root.
- The `findMaxPath` function recursively calculates the maximum path sum starting from the current node. It returns 0 if the current node is empty. It recursively calculates the maximum path sum in the left and right subtrees, avoiding negative path sums by taking the maximum of 0 and the result of the recursive calls.
- The maximum path sum is updated if the path through the current node is greater than the previously calculated maximum. Finally, it returns the maximum path sum starting from the current node.
- The algorithm uses a depth-first search approach to traverse the binary tree and find the maximum path sum efficiently.
"""

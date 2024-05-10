# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS Recursive Solution
        if not root:return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS Iterative Solution
        if not root:return 0
        stack=[[root,1]]
        height=0
        maxHeight=0
        while stack:
            curr,height=stack.pop()
            if curr.left: 
                stack.append([curr.left,height+1])
            if curr.right:
                stack.append([curr.right,height+1])
            maxHeight=max(height,maxHeight)
        return maxHeight
            
"""
Here's the tree structure:

       3
      / \
     9  20
       /  \
     15    7

Now, let's step through the code:

1. The root of the tree is `3`.

2. Since the root is not `None`, the function initializes a stack with `[root, 1]` and sets `height` and `maxHeight` to 0.

3. The while loop begins.

4. Pop the top of the stack: `curr = 3`, `height = 1`.

5. Since `3` has both left and right children, push them onto the stack with their heights incremented: `stack = [[9, 2], [20, 2]]`.

6. Update `maxHeight` to 2.

7. The loop continues.

8. Pop the top of the stack: `curr = 20`, `height = 2`.

9. `20` has both left and right children, so push them onto the stack with their heights incremented: `stack = [[9, 2], [15, 3], [7, 3]]`.

10. Update `maxHeight` to 3.

11. The loop continues.

12. Pop the top of the stack: `curr = 7`, `height = 3`.

13. `7` has no children, so the stack becomes: `stack = [[9, 2], [15, 3]]`.

14. Update `maxHeight` to 3.

15. The loop continues.

16. Pop the top of the stack: `curr = 15`, `height = 3`.

17. `15` has no children, so the stack becomes: `stack = [[9, 2]]`.

18. Update `maxHeight` to 3.

19. The loop continues.

20. Pop the top of the stack: `curr = 9`, `height = 2`.

21. `9` has no children, so the stack becomes empty.

22. Update `maxHeight` to 3.

23. The loop exits.

24. Return `maxHeight`, which is 3.

So, the maximum depth of the binary tree is 3.
"""
            
            

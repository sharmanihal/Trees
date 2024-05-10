class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Breadth First Approach
        if not root:return 0
        queue = deque([[root,1]])  
        height=maxHeight=0
        while queue:
            curr,height=queue.popleft()
            if curr.left:
                queue.append([curr.left,height+1])
            if curr.right:
                queue.append([curr.right,height+1])
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

2. Since the root is not `None`, the function initializes a queue with `[[root, 1]]` and sets `height` and `maxHeight` to 0.

3. The while loop begins.

4. Dequeue the front of the queue: `curr = 3`, `height = 1`.

5. `3` has both left and right children, so enqueue them with their heights incremented: `queue = [[9, 2], [20, 2]]`.

6. Update `maxHeight` to 2.

7. The loop continues.

8. Dequeue the front of the queue: `curr = 9`, `height = 2`.

9. `9` has no children, so the queue becomes `queue = [[20, 2]]`.

10. Update `maxHeight` to 2.

11. The loop continues.

12. Dequeue the front of the queue: `curr = 20`, `height = 2`.

13. `20` has both left and right children, so enqueue them with their heights incremented: `queue = [[15, 3], [7, 3]]`.

14. Update `maxHeight` to 3.

15. The loop continues.

16. Dequeue the front of the queue: `curr = 15`, `height = 3`.

17. `15` has no children, so the queue becomes `queue = [[7, 3]]`.

18. Update `maxHeight` to 3.

19. The loop continues.

20. Dequeue the front of the queue: `curr = 7`, `height = 3`.

21. `7` has no children, so the queue becomes empty.

22. Update `maxHeight` to 3.

23. The loop exits.

24. Return `maxHeight`, which is 3.

So, the maximum depth of the binary tree using BFS is also 3.
"""

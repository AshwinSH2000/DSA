# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
i just solved max depth. isnt this very similar to that?
replace max with min... that leads to a small problem
1st approach was to counter that (currently commented). 
2nd approach is slightly better. (to avoid float(inf))
3rd approach is BFS which is the fastest
'''
# Approach 3
from collections import deque

class Solution: 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)]) #storing node and its depth together

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

# Approach 2
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         if not root.left:
#             return 1+self.minDepth(root.right)
#         if not root.right:
#             return 1+self.minDepth(root.left)
#         return 1+min(self.minDepth(root.left), self.minDepth(root.right))


# Approach 1
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
        
#         leftDepth = self.minDepth(root.left)
#         rightDepth = self.minDepth(root.right)

#         if leftDepth == 0 and rightDepth == 0:
#             return 1
#         if leftDepth == 0:
#             leftDepth = float(inf)
#         elif rightDepth == 0:
#             rightDepth = float(inf)

#         return 1+min(leftDepth, rightDepth)
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
i just solved max depth. isnt this very similar to that?
replace max with min
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if leftDepth == 0 and rightDepth == 0:
            return 1
        if leftDepth == 0:
            leftDepth = float(inf)
        elif rightDepth == 0:
            rightDepth = float(inf)

        return 1+min(leftDepth, rightDepth)
        
        
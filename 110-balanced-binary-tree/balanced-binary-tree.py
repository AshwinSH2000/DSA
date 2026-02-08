# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
need a separate recursive function because the given just returns bool. 
three things to remember in the recursive function. 
1. if the leftsubtree returns -1, immediately propagate it. no further checking needed. 
2. if the rightsubtree returns -1, immediately propagate it. no further checking needed. 
3. if the difference in the left and right subtree comes out to be > 1, return -1. (this is the origin of the actual -1 that gets propagated throughout)
4. if none of these match, then it means the difference in height is actually <= 1. so just return the maxheight + 1
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.checkNode(root) != -1
        


    def checkNode(self, root) -> int:
        
        if root is None: 
            return 0

        leftDepth = self.checkNode(root.left)
        if leftDepth == -1:
            return -1
        
        rightDepth = self.checkNode(root.right)
        if rightDepth == -1:
            return -1

        difference = abs(leftDepth-rightDepth)
        if difference > 1:
            return -1

        return 1+max(leftDepth, rightDepth)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
approach: normal bfs but rather than adding the entire list of level order nodes, add their averages
'''
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #but this is mostly not needed because the min no of nodes is 1
        # if not root:
        #     return []

        q = []
        avgs = []

        q.append(root)
        while q:
            Sum = 0
            level_nodes = len(q)
            i=0
            while i < level_nodes:
                # i had not put pop(0) when i coded it for the first time.
                # crucial error.. can be overlooked
                node = q.pop(0)
                Sum = Sum + node.val
                i+=1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avgs.append(Sum/level_nodes)
            
        return avgs

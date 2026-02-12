# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
what i initially thought...
to find out the parent when you pop the child. but this is hella inefficient but it works

refined thought: kinda opposite. scan children when uou pop the parent. so that time you will have access to both! 
version 1 is shitty code but works. will refine it when i get time to revise this q again.
'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append(root)
        

        while q:
            level_nodes_len = len(q)
            found_x_parent, found_y_parent = None, None

            while level_nodes_len > 0:
                node = q.popleft()
                level_nodes_len -= 1

                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False #because they are siblings
                
                if node.left and node.left.val == x:
                    found_x_parent = node.val 
                
                if node.left and node.left.val == y:
                        found_y_parent = node.val

                if node.right and node.right.val == x:
                    found_x_parent = node.val 
                
                if node.right and node.right.val == y:
                        found_y_parent = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            #after coming out of loop, check found_x/y_parent values
            if found_x_parent is None and found_y_parent is not None:
                return False
            elif found_x_parent is not None and found_y_parent is None:
                return False
            elif found_x_parent is not None and found_y_parent is not None:
                if found_x_parent == found_y_parent:
                    return False # they are siblings
                else:
                    return True
            else:
                pass

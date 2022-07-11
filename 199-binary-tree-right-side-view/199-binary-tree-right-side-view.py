# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, max_level = [], -1
        
        def traverse_tree(node, level):
            nonlocal res, max_level
            if not node:
                return
            if max_level < level:
                res.append(node.val)
                max_level = level
            traverse_tree(node.right, level + 1)
            traverse_tree(node.left, level + 1)
        
        traverse_tree(root, 0)
        return res
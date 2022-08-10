# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)
    def sortedArrayToBSTHelper(self, nums, floor, ceiling):
        if floor > ceiling: return None
        middleIndex = (floor + ceiling) // 2
        n = TreeNode(nums[middleIndex])
        n.left = self.sortedArrayToBSTHelper(nums, floor, middleIndex - 1)
        n.right = self.sortedArrayToBSTHelper(nums, middleIndex + 1, ceiling)
        return n
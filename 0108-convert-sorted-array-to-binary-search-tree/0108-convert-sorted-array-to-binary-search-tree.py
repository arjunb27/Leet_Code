# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)        
        
        # root is always at mid for a height-balanced
        
        # subarray
        # mid = n//2
        # root = TreeNode(nums[mid])
        # if mid>0: root.left = self.sortedArrayToBST(nums[:mid])
        # if mid<n-1: root.right = self.sortedArrayToBST(nums[1+mid:])        
        # return root
        
        # use index to save space
        def h(start, end):
            if start>end: return
            mid = (start + end)//2
            root = TreeNode(nums[mid])
            if start==end: return root
            root.left = h(start, mid-1)
            root.right = h(mid+1, end)
            return root
        
        return h(0, n-1)
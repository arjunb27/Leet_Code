class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      ans.append(root.val)
      root = root.right

    return ans
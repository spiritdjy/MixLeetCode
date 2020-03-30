# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        max_depth = [0]

        def resc_depth(root, n):
            if root:
                n += 1
                if n > max_depth[0]:
                    max_depth[0] = n
                resc_depth(root.left, n)
                resc_depth(root.right, n)

        resc_depth(root, 0)

        return max_depth[0]

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 0)]
        max_depth = 0

        while stack:
            node, length = stack.pop()
            length += 1
            if length > max_depth:
                max_depth = length
            if node.left:
                stack.append((node.left, length))
            if node.right:
                stack.append((node.right, length))

        return max_depth



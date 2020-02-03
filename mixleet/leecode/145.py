"""
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        left = self.postorderTraversal(root.left) if root.left else []
        right = self.postorderTraversal(root.right) if root.right else []
        return left + right + [root.val]

    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []

        stack = [(root, 0)]
        ret = []
        while stack:
            node, state = stack.pop()
            if state == 1:
                ret.append(node.val)
            else:
                stack.append((node, 1))
                if node.right:
                    stack.append((node.right, 0))
                if node.left:
                    stack.append((node.left, 0))

        return ret


def test():
    def case1():
        x3 = TreeNode(3)
        x2 = TreeNode(2)
        x2.left = x3
        x1 = TreeNode(1)
        x1.right = x2
        assert Solution().postorderTraversal(x1) == [3,2,1]

    def case2():
        x3 = TreeNode()

    case1()


if __name__ == '__main__':
    test()
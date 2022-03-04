# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        if not root:
            return
        res = [root.val]

        def maxSum(root):
            leftb = -1000
            rightb = -1000
            if not root.left and not root.right:
                return root.val
            if root.left:
                leftb = maxSum(root.left)
            if root.right:
                rightb = maxSum(root.right)
            split = leftb + root.val + rightb
            returned = max(leftb + root.val, rightb + root.val, root.val)
            res[0] = max(res[0], split, leftb, rightb, returned)
            return returned

        maxSum(root)
        return res[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

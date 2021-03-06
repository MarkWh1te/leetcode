# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST_helper(self, root, low, up) -> bool:
        """
        return min , max,is_bst
        """
        if not root:
            return True
        return (root.val < up and root.val > low) and self.isValidBST_helper(root.left, low, root.val) and self.isValidBST_helper(root.right, root.val, up)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST_helper(root, float('-inf'), float('inf'))

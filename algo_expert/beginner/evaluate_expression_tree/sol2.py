# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value
    left_val = evaluateExpressionTree(tree.left)
    right_val = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left_val + right_val
    elif tree.value == -2:
        return left_val - right_val
    elif tree.value == -3:
        return int(left_val / right_val)  # NOTE: this round leads to incorrect results
    return left_val * right_val


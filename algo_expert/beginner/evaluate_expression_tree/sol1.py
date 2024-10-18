# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    def operant(left, right, val):
        if val == -1:
           return left + right
        elif val == -2:
            return left - right
        elif val == -3:
            return int(left / right)  # NOTE: this round leads to incorrect results
        elif val == -4:
            return left * right
        else:
            return val

    if tree.left is None and tree.right is None:
        return tree.value
    
    left_val = evaluateExpressionTree(tree.left)
    right_val = evaluateExpressionTree(tree.right)
    return operant(left_val, right_val, tree.value)

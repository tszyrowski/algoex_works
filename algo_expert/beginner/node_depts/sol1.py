def nodeDepths(root):
    """
    Computes the sum of all node depths in the binary tree.

    :param root: BinaryTree, the root of the binary tree.
    :return: Integer, the sum of the depths of all nodes.
    """
    return getBranchDepth(root, 0)


def getBranchDepth(node, current_depth):
    """
    Helper function to calculate the sum of node depths.

    :param node: BinaryTree, the current node in the tree.
    :param current_depth: Integer, the depth of the current node.
    :return: Integer, the sum of depths for all nodes.
    """
    if node is None:
        return 0

    # Calculate the depth of the current node and recurse for left and right children
    return current_depth + getBranchDepth(node.left, current_depth + 1) + getBranchDepth(node.right, current_depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


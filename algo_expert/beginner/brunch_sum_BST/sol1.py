class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    """
    Computes the branch sums for each branch from root to leaf.

    :param root: BinaryTree, the root of the binary tree.
    :return: List of integers, each representing the sum of a branch.
    """
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, running_sum, sums):
    """
    Helper function to calculate branch sums using recursion.

    :param node: BinaryTree, the current node in the tree.
    :param running_sum: int, the sum accumulated from the root to the current node.
    :param sums: list of int, stores the branch sums when leaf nodes are reached.
    """
    if node is None:
        return
    
    # Update the running sum with the current node's value
    new_running_sum = running_sum + node.value
    
    # If the node is a leaf, append the running sum to the sums list
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    
    # Otherwise, recursively call on the left and right children
    calculateBranchSums(node.left, new_running_sum, sums)
    calculateBranchSums(node.right, new_running_sum, sums)
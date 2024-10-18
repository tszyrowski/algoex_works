def nodeDepths(root):
    """
    Computes the sum of all node depths in a binary tree.
    
    :param root: BinaryTree, the root of the binary tree.
    :return: int, the sum of the depths of all nodes.
    """
    # Start the recursion with depth 0 and an empty list to collect depths
    nodes_depths = getBranchDepth(root, [], 0)
    return sum(nodes_depths)


def getBranchDepth(node, nodes_depths, current_depth):
    if node is None:
        return  # Don't append anything when you hit None
    
    # Append the current depth for this node
    nodes_depths.append(current_depth)
    
    # Recurse on left child with incremented depth
    if node.left is not None:
        getBranchDepth(node.left, nodes_depths, current_depth + 1)
    
    # Recurse on right child with incremented depth
    if node.right is not None:
        getBranchDepth(node.right, nodes_depths, current_depth + 1)

    return nodes_depths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

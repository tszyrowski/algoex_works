def findClosestValueInBst(tree, target):
    # Write your code here.
    node = tree
    closest = float("inf")

    while node is not None:
        closest = node.value if abs(node.value-target) < abs(closest-target) else closest
        if node.value < target:
            node = node.right
            continue
        node = node.left
    return closest

    

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def nodeDepths(root, depth=0):
    return 0 if root is None else depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)


def nodeDepths(root):
    queue = [(root, 0)]
    runningSumDepth = 0
    while queue:
        curNode, curDepth = queue.pop(0)
        runningSumDepth += curDepth
        if curNode.left:
            queue.append((curNode.left, curDepth+1))
        if curNode.right:
            queue.append((curNode.right, curDepth+1))
    return runningSumDepth


def nodeDepths(root):
    stack = [(root, 0)]
    sum = 0
    while stack:
        node, depth = stack.pop()
        sum += depth
        if node.left: stack.append((node.left, depth+1))
        if node.right: stack.append((node.right, depth+1))
    return sum



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
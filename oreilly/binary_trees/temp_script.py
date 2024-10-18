A = [31, 41, 59, 26, 53, 58, 97]
print(26 in A)   # search() success
print(55 in A)   # search() failure
A.remove(26)     # remove()
print(A)
A.append(62)     # insert()
print(A)

class BinaryNode:
    def __init__(self, val):
        self.value = val
        self.left  = None
        self.right = None
    
    def __str__(self):
        return '[{}]'.format(self.value)
    
    def search(self, v):
        if self.value == v:
            return True
        if v < self.value and self.left:
            return self.left.search(v)
        if v > self.value and self.right:
            return self.right.search(v)
        return False
  
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, v):
        self.root=self._insert(self.root, v)

    def _insert(self, node, v):
        if node is None:
            return BinaryNode(v)

        if v <= node.value:
            node.left=self._insert(node.left,v)
        else:
            node.right=self._insert(node.right,v)
        return node  
    
    def __contains__(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right

        return False
    
    def search(self, v):
        if self.root is None:
            return False
        return self.root.search(v)

    def _remove_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._remove_min(node.left)
        return node
    
    def remove(self, v):
        self.root = self._remove(self.root, v)
    

    def _remove(self, node, v):
        if node is None:
            return None

        if v < node.value:
            node.left = self._remove(node.left, v)
        elif v > node.value:
            node.right = self._remove(node.right, v)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

        original = node

        # find SMALLEST child in right subtree
        node = node.right
        while node.left:
            node = node.left

        node.right = self._remove_min(original.right)
        node.left = original.left
        return node


bst = BinaryTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(40)
print("Root: ", bst.root)
print(bst.root.left)
print(bst.root.right)
print(bst.root.right.right)
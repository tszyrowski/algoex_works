
**Find Closest Value In BST**

Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each **BST** node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid **BST** node if and only if it satisfies the **BST** property: its `value` is strictly greater than the values of every node to its left; its `value` is less than or equal to the values of every node to its right; and its children nodes are either valid **BST** nodes themselves or `None` / `null`.

### Sample Input
```
tree = 10
       /  \
      5   15
     / \  / \
    2  5 13 22
   /       \
  1        14

target = 12
```

### Sample Output
```
13
```

## Q:
starting with this code:

def findClosestValueInBst(tree, target):
    # Write your code here.
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


can you propose optimal solution?

## A:

Let's build an optimal solution for the problem of finding the closest value to a target in a Binary Search Tree (BST).

### Key Observations:

1. **Binary Search Tree Property**:
   - In a BST, for any given node:
     - The left child contains values smaller than the node’s value.
     - The right child contains values greater than or equal to the node’s value.
   
2. **Optimal Traversal**:
   - Because of this property, we can traverse the tree efficiently without needing to explore all nodes. Specifically:
     - If the target is less than the current node’s value, we only need to explore the left subtree.
     - If the target is greater than the current node’s value, we only need to explore the right subtree.
   
3. **Goal**:
   - As we traverse the tree, we maintain a variable tracking the closest value we’ve seen to the target.

### Approach:

- **Iterative Approach**: This avoids potential stack overflow from deep recursion (common in recursive solutions for large trees) and provides better control over the flow.

### Time Complexity:
- **Time complexity**: `O(log n)` for balanced trees because at each step we halve the search space. In the worst case (unbalanced tree), the complexity could be `O(n)`, where `n` is the number of nodes.
- **Space complexity**: `O(1)` for the iterative version (no recursion stack).

### Code Implementation:

```python
def findClosestValueInBst(tree, target):
    """
    Finds the closest value to the target in the BST.
    
    :param tree: BST, the root node of the binary search tree.
    :param target: int, the target value to find the closest value to.
    :return: int, the value in the BST closest to the target.
    """
    closest = tree.value
    current_node = tree

    while current_node is not None:
        # Update closest if current node is closer to target
        if abs(target - current_node.value) < abs(target - closest):
            closest = current_node.value
        
        # Move left if target is smaller than the current value
        if target < current_node.value:
            current_node = current_node.left
        # Move right if target is larger than the current value
        elif target > current_node.value:
            current_node = current_node.right
        # If the target matches the current value, return immediately
        else:
            break
    
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Explanation:

1. **Closest Tracking**: We initialize `closest` with the value of the root node (`tree.value`), as it’s the best guess at the beginning.

2. **Iterative Search**:
   - We use a `while` loop to traverse the tree. The variable `current_node` helps us navigate through the tree.
   - At each step, we compare the current node’s value with the target:
     - If the target is less than the current node's value, we move left.
     - If the target is greater, we move right.
   - If the current node’s value is exactly equal to the target, we can terminate early since we’ve found the closest possible value.

3. **Updating Closest**: At each node, we check if the current node's value is closer to the target than the previously stored `closest` value, and if so, we update `closest`.

### Example:

For the BST:
```
       10
      /  \
     5   15
    / \  / \
   2  5 13 22
  /       \
 1        14
```

If the target is `12`, the traversal would go like this:
- Start at root (`10`): update `closest` to `10`.
- Move right to `15`: check if `15` is closer to `12` (it's not, `10` is still closer).
- Move left to `13`: update `closest` to `13` since `13` is closer to `12` than `10`.
- Move left again to `14`, but `13` is still closer, so we stop and return `13`.

### Time Complexity Recap:

- **Balanced Tree**: In a balanced tree, we only need to explore one path, so the complexity is `O(log n)`.
- **Unbalanced Tree**: In the worst case (unbalanced tree), we might have to explore all nodes, resulting in a complexity of `O(n)`.

This solution ensures efficiency while maintaining clarity and simplicity. Let me know if you need further clarifications!
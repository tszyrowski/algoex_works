# Binary Trees: Working with Binary Search Trees
## Step 1 of 3
### Constructing Binary Search Trees

Because the Python list is so flexible, it is commonly used inefficiently. A common lab is to both add values to a list and remove values from a list; later, you just want to determine whether a value is contained in the list.

```python 
A = [31, 41, 59, 26, 53, 58, 97]
print(26 in A)   # search() success
print(55 in A)   # search() failure
A.remove(26)     # remove()
print(A)
A.append(62)     # insert()
print(A)
quit()
```
Searching for a value in a Python list starts at the index location 0 and proceeds until the value has been found in the list, or the end of the list has been reached. Removing a value follows the same procedure, but then removing a value from the middle requires that all values to the right are moved down. Appending a value to the end of a list is efficient, but the values in the list remain unordered and, over time, searching and removal become less and less efficient.

A Binary Search Tree offers a more efficient data structure that supports the efficient implementation of insert(), remove(), and search() operations.

A binary search tree is composed of binary nodes, each of which contains a value and has a left child and a right child, each of which is a binary node. The following is a binary search tree containing seven binary nodes:

```
tree =  
        53
      /   \
     31    59
    / \   / \
   26 41 58  97
```

Each circle represents a binary node, and the number drawn within the circle is the value stored by that binary node. The node at the top, labeled **53** is the root node of the binary search tree. This root node has two children. The left child is the binary node containing the value 31 and the right child is the binary node containing the value 59. As you can see the value in the root's left child is smaller than or equal to the value in the root. Similarly, the value in the root's right child is larger than or equal to the value in the root. This observation is known as the **_Binary Search Tree Property_**.

The node containing 31 also shares this property, since its left child is a node containing the value 26 and its right child contains the value 41. You can also confirm that the node containing 59 is larger than or equal to the value contained in its left child node, 58, and it is smaller than or equal to the value contained in its right child node, 97.

The _Binary Search Tree Property_ is a global property that applies to every `BinaryNode` in the tree.

This binary search tree contains four leaf nodes, that is, nodes such as 26 that have neither a left or a right child. Many people have commented that computer science trees are upside down, because the leaves are at the bottom, while the root is at the top.

Let's start writing code to implement binary search trees.

```python
class BinaryNode:
  def __init__(self, val):
    self.value = val
    self.left  = None
    self.right = None
  
  def __str__(self):
    return '[{}]'.format(self.value)
  
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
    
  # TODO: More BinaryTree
```
Each `BinaryNode` stores a value and references to the `left` and `right` child, should they exist. A `BinaryTree` class stores the `root` node of the tree. Note that the `insert(v)` method is defined for `BinaryTree`.

The `insert(v)` function invokes an internal function `_insert(self.root, v)` which handles all three sub-cases that arise. `insert(v)` returns a `BinaryNode`. The way to think about the `insert(v)` method is that "it inserts `v` into the binary search tree rooted at `self.root` and returns the root node of the resulting structure." If `self.root` is `None` the tree contains no nodes.

There are three cases to handle in `_insert(node, v)`:

- If `node` is `None`, then a new `BinaryNode` is returned to be the new root node of a tree.
- If `node` has a value, and `v` is smaller than or equal to node.value, then set `node.left` to be the node of the subtree that results when inserting `v` into `node.left`.
- If `node` has a value, and `v` is greater than `node.value`, then set `node.right` to be the node of the subtree that results when inserting `v` into `node.right`.

Let's try this out, by creating a binary search tree and inserting values one at a time.

```python
python -i tree.py
bst = BinaryTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(40)
print(bst.root)
print(bst.root.left)
print(bst.root.right)
print(bst.root.right.right)
quit()
```
The output should be:

```python
[20]
[10]
[30]
[40]
```
Initially the binary search tree, bst, has None as its root. When inserting 20 into an empty binary tree, the _insert(node,v) method simply returns a BinaryNode containing v, and this node becomes the root of the binary tree.

```
Sample Binary Tree =  
        20
```

Inserting 10 leads to the second of the three cases above, since 10 is smaller than or equal to the root value of 20.

```
Sample Binary Tree =  
        20
       /
      10
```

Inserting 30 leads to the third of the three cases above, since 30 is larger than or equal to the root value of 20.

```
Sample Binary Tree =  
        20
       /  \
      10  30
```

Now insert *40*. This value is greater than the root's value of *20*, so this value must be inserted into the right subtree of *20*. But there already is a node there whose value is *30*, which means that 40 will ultimately be placed in a node that becomes the right child of *30*.

```
Sample Binary Tree =  
        20
       /  \
      10  30
            \
            40
```

This resulting tree has a left subtree rooted at a node containing *10*, and it has a right subtree, rooted at a node containing *30*. Each subtree has the same structure as the original root, which is why a binary search tree is considered to be a recursive data structure. You can see that inserting values using this method will ensure that the binary search tree property continues to hold.

Now that a binary search tree exists, continue onward to learn how to search for values in the binary search tree.

## Binary Trees: Working with Binary Search Trees
## Step 2 of 3
### Searching Binary Search Trees

When searching for the values in a list, *A*, you might write code that looks like the following:
```python
def search(A, target):
  for i in range(len(A)):
    if A[i] == target:
      return True
  return False 
```
Since a list is a linear structure, it makes sense to start at the first index location and check increasing index locations until the desired value has been found. But what should you do for a binary search tree?
```
Sample Binary Tree =  
        20
       /  \
      10  30
            \
            40
```
Does the above tree contain the value **40**? Start by checking whether the root node contains this value. If it does, you can simply return `True`. But since the root node contains **20**, you have to decide what to do next. Since the value **40** is greater than or equal to **20**, you know from the binary search tree property that the value cannot possibly be in the left subtree of **20**, but it might yet be in the right subtree.

This right subtree is rooted at **30**, which is not the value you are looking for. If **40** exists, it could be found in the right-subtree of this node, which is rooted at the node **40**. There! You've found the value.
```python
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
  
  # TODO: More BinaryTree
```
By defining a `__contains__()` method in `BinaryTree`, I take advantage of the in operator provided by Python. This method belongs to the `BinaryTree` class. It starts with `node` set to the `root` of the binary search tree. As long as node is not `None`, the `while` loop will check whether `node` contains a value equal to the `target`, returning `True` if found.

If `node` doesn't contain `target`, then based on whether `target` is smaller than or greater than the value stored by `node`, `node` is set to either the `left` child of the `right` child. Note that it might be the case that there is no such child, in which case `node` is set to `None`.

Sample Binary Tree

A successful search for **40** starts at the root and continues downward to the right until that value is found in the highlighted leaf node above.

Let's try out this implementation:
```python
python -i tree.py
bst = BinaryTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(40)
print(30 in bst)    # success
print(15 in bst)    # failure
quit()
```
This efficient search implementation is not recursive. An alternate recursive implementation would require the following methods to be added to BinaryNode and BinaryTree:
```python
class BinaryNode:
  def search(self, v):
    if self.value == v:
      return True
    if v < self.value and self.left:
      return self.left.search(v)
    if v > self.value and self.right:
      return self.right.search(v)
    return False

class BinaryTree:
  def search(self, v):
    if self.root is None:
      return False
    return self.root.search(v)
```
The non-recursive implementation I provide is more efficient and brief.

Now that you can insert values into a binary search tree and search for them again, it is time to see how values can be removed from a binary search tree. Continue onward to learn how!

---
## Binary Trees: Working with Binary Search Trees
## Step 3 of 3
### Removing a value from a Binary Search Tree

Deleting a value from a Python list is straightforward: Once the value is removed, all other values are just shifted down one location. However, removing a value from a binary search tree is complicated.

What if you want to remove the value 19 from the following binary search tree?

```
Sample Binary Tree =  
        19
       /  \
     14   53
    / \   / \
   3  15 26 58
          \
          29
```

This is the value stored by the root node. You can't just remove this node from the binary search tree, since there will be two "orphaned" subtrees, and there can only be a single root in a binary search tree. In addition, you have to make sure that the resulting structure maintains the global binary search tree property.

Let's solve a smaller problem first, namely, removing the minimum value from a subtree rooted at a given `BinaryNode`. For convenience, place this recursive method in the `BinaryTree` class. Given a `BinaryNode`, `node`, that represents the root of a subtree with N > 0 values, there are only two cases to consider:

- If `node` has no `left` child, then it itself contains the smallest value in the subtree. To remove the value, then, you only need to return the `right` subtree, which contains the other N-1 values.
- If node has a left child, then set node.left to be the subtree that results when removing the minimum value from it. The implementation is below:
```python
  def _remove_min(self, node):
    if node.left is None:
      return node.right

    node.left = self._remove_min(node.left)
    return node
    
  # TODO: More BinaryTree
```
Because this method is only invoked on non-empty subtrees, you do not have to worry about the case when `node` is `None`. How does this function help?

Let's return to the original tree.

```
Sample Binary Tree =  
        19
       /  \
     14   53
    / \   / \
   3  15 26 58
          \
          29
```

Consider the following binary search tree that should be the result of removing the value **19** from the above binary search tree:
```
Sample Binary Tree =  
        26
       /  \
     14   53
    / \   / \
   3  15 29 58
```

I've highlighted in yellow the original left subtree of three nodes, since this structure has not changed from the original tree. Now, look at the original right subtree:

```
   53
  /  \
 26  58
  \
  29
```

If you remove the minimum value from this subtree, you will produce the following, which matches the goal above:

```
   53
  /  \
 29  58
```

Now we have a strategy to move forward: To remove a value from a binary search tree, first locate it within the binary search tree. If the value is not found, then nothing needs to be done. Otherwise, the only nodes in the tree that will be affected by removing the value contained in that node are the direct `left` and `right` subtrees.

Start by adding the following method to `BinaryTree`:
```
  def remove(self, v):
    self.root = self._remove(self.root, v)
  
  # TODO: More BinaryTree
```
This method has the standard structure for a recursive implementation, calling a helper method `_remove(v)` that you will add next. This recursive method removes `v` (should it exist) from the subtree rooted at `node`, and returns the (potentially new) root of the modified subtree.
```python
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

      # Last case is hardest
      # TBA
    return node
```
This code covers the easy cases. First, if `node` is `None` then there is nothing to be done, so the code just returns `None`. If `node` exists and `v` is smaller than `node.value`, then set `node.left` to be the root node of the subtree resulting when removing `v` from `node.left`. Similarly, if `v` is larger than `node.value`, then set `node.right` to be the root node of the subtree resulting when removing `v` from `node.right`.

In the third case, `v` equals `node.value`, and there are two easy cases to handle right away. It could be that `node.left` is `None`, so the function simply returns the right subtree, `node.right`. Similarly, if `node.right` is `None`, the function simply returns the left subtree, `node.left`.

Note that in all cases, the function returns `node`, which is the original node at the top of the subtree when `_remove()` was invoked.

The last case is more difficult, when the function finds a node that needs to be removed, but it has both a `left` and a `right` child. The trick, here, is to find the smallest child in the right subtree of `node`. This `node` will be the one that ultimately replaces the one being removed.

In fact, after remembering `original`, the `while` loop changes `node` to refer to this minimum value in the right subtree for the original node to be removed.
```python
      # keep track of original node
      original = node

      # find SMALLEST child in right subtree
      node = node.right
      while node.left:
        node = node.left

      node.right = self._remove_min(original.right)
      node.left = original.left
```
Once this value is known, you can now:

- Remove the minimum value from `original.right`, and the resulting subtree becomes the right-subtree for node;
- Because the original left subtree is unchanged, make sure to set `node.left` to `original.left`. Note that node is now the root node of the modified subtree, and it will be returned by this function.

WHEW. This lab covered a lot of ground. Let's confirm `remove(v)` works by showing the binary search tree that results when removing values. Here is the original tree:
```
        19
       /  \
     14   53
    / \   / \
   3  15 26 58
          \
          29
```
Delete 19 to produce:
```
        26
       /  \
     14   53
    / \   / \
   3  15 29 58
```
Now remove 53 to produce:
```
Sample Binary Tree =  
        26
       /  \
     14   58
    / \   / 
   3  15 29 
```
Try it out! The following creates a tree that has 20 as its root; the left node contains the value 10, and the right node is a subtree rooted at a node 30, with a right child containing the value 40.
```python
python -i tree.py
bst = BinaryTree()
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(10)
bst.remove(20)  # remove root
print(bst.root.value,'is 30')
quit()
```
After removing the value stored in the root node, the tree is adjusted to have 30 as the new root node value.

This completes this introduction to inserting, removing, and searching for values in a binary search tree.
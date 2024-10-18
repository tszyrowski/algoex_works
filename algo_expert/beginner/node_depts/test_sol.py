import json
from sol1 import nodeDepths, BinaryTree

def build_tree_from_json(json_tree):
    """
    Rebuilds the binary tree from JSON input.

    :param json_tree: The JSON representation of the tree.
    :return: The root node of the reconstructed binary tree.
    """
    nodes = {node["id"]: BinaryTree(node["value"]) for node in json_tree["nodes"]}
    
    for node in json_tree["nodes"]:
        current_node = nodes[node["id"]]
        if node["left"]:
            current_node.left = nodes[node["left"]]
        if node["right"]:
            current_node.right = nodes[node["right"]]
    
    return nodes[json_tree["root"]]

if __name__ == "__main__":
    # Load the JSON structure
    tree_data = json.loads("""
    {
      "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": "10", "right": null, "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "7", "left": null, "right": null, "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "9", "left": null, "right": null, "value": 9},
        {"id": "10", "left": null, "right": null, "value": 10}
      ],
      "root": "1"
    }""")

    # Rebuild the tree from JSON
    root_node = build_tree_from_json(tree_data)

    # Now call the branchSums function
    result = nodeDepths(root_node)

    print(result)  # Output the branch sums for inspection

import json
from sol1 import evaluateExpressionTree, BinaryTree

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
    "tree": {
        "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": -1},
        {"id": "2", "left": null, "right": null, "value": 2},
        {"id": "3", "left": "4", "right": "5", "value": -2},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "5", "left": null, "right": null, "value": 5}
        ],
        "root": "1"
    }
    }
    """)

    tree_data_2 = json.loads("""
    {
    "tree": {
        "nodes": [
        {"id": "1", "left": "2", "right": "9", "value": -4},
        {"id": "2", "left": "4", "right": "3", "value": -1},
        {"id": "3", "left": null, "right": null, "value": 8},
        {"id": "4", "left": "5", "right": "6", "value": -1},
        {"id": "5", "left": null, "right": null, "value": 7},
        {"id": "6", "left": "7", "right": "8", "value": -2},
        {"id": "7", "left": null, "right": null, "value": 22},
        {"id": "8", "left": null, "right": null, "value": 5},
        {"id": "9", "left": "10", "right": "11", "value": -3},
        {"id": "10", "left": null, "right": null, "value": 100},
        {"id": "11", "left": "12", "right": "13", "value": -2},
        {"id": "12", "left": null, "right": null, "value": 42},
        {"id": "13", "left": "14", "right": "15", "value": -3},
        {"id": "14", "left": "16", "right": "17", "value": -4},
        {"id": "15", "left": null, "right": null, "value": 2},
        {"id": "16", "left": null, "right": null, "value": 3},
        {"id": "17", "left": null, "right": null, "value": 9}
        ],
        "root": "1"
    }
    }
    """
    )
    tree_data_fail = json.loads("""
        {
        "tree": {
            "nodes": [
            {"id": "1", "left": "9", "right": "3", "value": -3},
            {"id": "9", "left": null, "right": null, "value": 9},
            {"id": "3", "left": "4", "right": "6", "value": -2},
            {"id": "4", "left": null, "right": null, "value": 4},
            {"id": "6", "left": null, "right": null, "value": 6}
            ],
            "root": "1"
        }
        }
        """
    )

    # Rebuild the tree from JSON
    root_node = build_tree_from_json(tree_data)

    # Now call the branchSums function
    result = evaluateExpressionTree(root_node)

    print(result)  # Output the branch sums for inspection
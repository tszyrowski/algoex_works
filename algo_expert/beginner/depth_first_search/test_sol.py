import json
from sol1 import Node

def build_graph_from_json(graph_data):
    nodes_dict = {node_data["id"]: node_data for node_data in graph_data["graph"]["nodes"]}

    start_node_id = graph_data["graph"]["startNode"]
    start_node_data = nodes_dict[start_node_id]
    root = Node(start_node_data["value"])
    build_graph_recursively(root, start_node_data, nodes_dict)
    return root

def build_graph_recursively(node, node_data, nodes_dict):
    for child_id in node_data.get("children", []):
        child_node_data = nodes_dict[child_id]
        node.addChild(child_node_data["value"])
        child_node = node.children[-1]  # Get the last added child
        build_graph_recursively(child_node, child_node_data, nodes_dict)

def test_depthFirstSearch_1():
    # Load the graph data from the JSON input.
    graph_data = json.loads("""
    {
    "graph": {
        "nodes": [
        {"children": ["B", "C", "D"], "id": "A", "value": "A"},
        {"children": ["E", "F"], "id": "B", "value": "B"},
        {"children": [], "id": "C", "value": "C"},
        {"children": ["G", "H"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": ["I", "J"], "id": "F", "value": "F"},
        {"children": ["K"], "id": "G", "value": "G"},
        {"children": [], "id": "H", "value": "H"},
        {"children": [], "id": "I", "value": "I"},
        {"children": [], "id": "J", "value": "J"},
        {"children": [], "id": "K", "value": "K"}
        ],
        "startNode": "A"
    }
    }
    """)
    expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    root = build_graph_from_json(graph_data)
    result = root.depthFirstSearch([])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_depthFirstSearch_2():
    # Load the graph data from the JSON input.
    graph_data = json.loads("""
    {
    "graph": {
        "nodes": [
        {"children": ["B", "C"], "id": "A", "value": "A"},
        {"children": ["D"], "id": "B", "value": "B"},
        {"children": [], "id": "C", "value": "C"},
        {"children": [], "id": "D", "value": "D"}
        ],
        "startNode": "A"
    }
    }
    """)
    expected = ["A", "B", "D", "C"]
    root = build_graph_from_json(graph_data)
    result = root.depthFirstSearch([])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_depthFirstSearch_3():
    # Load the graph data from the JSON input.
    graph_data = json.loads("""
    {
    "graph": {
        "nodes": [
        {"children": ["B", "C", "D", "E"], "id": "A", "value": "A"},
        {"children": [], "id": "B", "value": "B"},
        {"children": ["F"], "id": "C", "value": "C"},
        {"children": [], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": [], "id": "F", "value": "F"}
        ],
        "startNode": "A"
    }
    }
    """)
    expected = ["A", "B", "C", "F", "D", "E"]
    root = build_graph_from_json(graph_data)
    result = root.depthFirstSearch([])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_depthFirstSearch_4():
    # Load the graph data from the JSON input.
    graph_data = json.loads("""
    {
    "graph": {
        "nodes": [
        {"children": ["B"], "id": "A", "value": "A"},
        {"children": ["C"], "id": "B", "value": "B"},
        {"children": ["D", "E"], "id": "C", "value": "C"},
        {"children": ["F"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": [], "id": "F", "value": "F"}
        ],
        "startNode": "A"
    }
    }
    """)
    expected = ["A", "B", "C", "D", "F", "E"]
    root = build_graph_from_json(graph_data)
    result = root.depthFirstSearch([])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

def test_depthFirstSearch_5():
    # Load the graph data from the JSON input.
    graph_data = json.loads("""
    {
    "graph": {
        "nodes": [
        {"children": ["B", "C", "D", "E", "F"], "id": "A", "value": "A"},
        {"children": ["G", "H", "I"], "id": "B", "value": "B"},
        {"children": ["J"], "id": "C", "value": "C"},
        {"children": ["K", "L"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": ["M", "N"], "id": "F", "value": "F"},
        {"children": [], "id": "G", "value": "G"},
        {"children": ["O", "P", "Q", "R"], "id": "H", "value": "H"},
        {"children": [], "id": "I", "value": "I"},
        {"children": [], "id": "J", "value": "J"},
        {"children": ["S"], "id": "K", "value": "K"},
        {"children": [], "id": "L", "value": "L"},
        {"children": [], "id": "M", "value": "M"},
        {"children": [], "id": "N", "value": "N"},
        {"children": [], "id": "O", "value": "O"},
        {"children": ["T", "U"], "id": "P", "value": "P"},
        {"children": [], "id": "Q", "value": "Q"},
        {"children": ["V"], "id": "R", "value": "R"},
        {"children": [], "id": "S", "value": "S"},
        {"children": [], "id": "T", "value": "T"},
        {"children": [], "id": "U", "value": "U"},
        {"children": ["W", "X", "Y"], "id": "V", "value": "V"},
        {"children": [], "id": "W", "value": "W"},
        {"children": ["Z"], "id": "X", "value": "X"},
        {"children": [], "id": "Y", "value": "Y"},
        {"children": [], "id": "Z", "value": "Z"}
        ],
        "startNode": "A"
    }
    }
    """)
    expected = ["A", "B", "G", "H", "O", "P", "T", "U", "Q", "R", "V", "W", "X", "Z", "Y", "I", "C", "J", "D", "K", "S", "L", "E", "F", "M", "N"]
    root = build_graph_from_json(graph_data)
    result = root.depthFirstSearch([])
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"

if __name__ == "__main__": 
    import pytest
    pytest.main(["-s", "-v", __file__])
import binarytree
from graphviz import Digraph

# Most expencive path in bst

MAX_SUM = float("-inf")
MAX_SUM_PATH = []


def dfs(node, current_path: list, current_weight):

    global MAX_SUM_PATH, MAX_SUM

    if not node:
        return

    current_path.append(node.value)
    current_weight += node.value

    # If left & right clildren are none
    # we have arrived at leaf node
    if not node.left and not node.right:

        # Update weight and path if
        # current values are bigger then previous
        if current_weight > MAX_SUM:
            MAX_SUM = current_weight
            # create a copy of a current path
            MAX_SUM_PATH = current_path[:]

    dfs(node.left, current_path, current_weight)
    dfs(node.right, current_path, current_weight)

    # Delete last elements from old path
    current_path.pop()
    current_weight -= node.value


def find_max_sum_path(root):
    if not root:
        return [], 0
    dfs(root, [], 0)

# Visualize path
def graphviz_colored_path(bst, max_path,) -> Digraph:

    digraph = Digraph()

    for node in bst:
        node_id = str(id(node))

        digraph.node(node_id, label=str(node.value))

        color_left = "black"
        color_right = "black"

        if node.left is not None:
            if node.left.value in max_path:
                color_left = "red"
            digraph.edge(f"{node_id}", f"{id(node.left)}", color=color_left)

        if node.right is not None:
            if node.right.value in max_path:
                color_right = "red"
            digraph.edge(f"{node_id}", f"{id(node.right)}", color=color_right)

    return digraph


def main():
    root = binarytree.bst(height=4)

    if root is None:
        return

    find_max_sum_path(root)

    print("Max path: ", MAX_SUM_PATH, "\nMax weight: ", MAX_SUM)

    tree_as_colored_graph = graphviz_colored_path(root, MAX_SUM_PATH)
    tree_as_colored_graph.view()


if __name__ == "__main__":
    main()

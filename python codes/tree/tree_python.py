def add_key_property(nodes, fig_num):
    # Function to find all final nodes starting from a given node
    def find_final_nodes(node):
        final_nodes = set()
        stack = [node]
        while stack:
            current = stack.pop()
            next_successors = nodes.get(current, {}).get('successor', [])
            if next_successors:
                stack.extend(next_successors)
            else:
                final_nodes.add(current)
        return final_nodes

    # Iterate through each node to find those with multiple successors
    row_no = 1
    for node, props in nodes.items():
        successors = props.get('successor', [])
        if successors and len(successors) > 1:
            final_nodes = set()
            for successor in successors:
                final_nodes.update(find_final_nodes(successor))
            # Add 'key' if all final nodes converge to a single node
            if len(final_nodes) == 1:
                nodes[node]['key'] = f'row_num{row_no}'
                row_no += 1
    return nodes

# Define the input figures
nodes_fig1 = {
    'A': {'predecessor': None, 'successor': ['B']},
    'B': {'predecessor': 'A', 'successor': ['C', 'D']},
    'C': {'predecessor': 'B', 'successor': ['E']},
    'D': {'predecessor': 'B', 'successor': ['E']},
    'E': {'predecessor': ['C', 'D'], 'successor': None}
}

nodes_fig2 = {
    'A': {'predecessor': None, 'successor': ['B']},
    'B': {'predecessor': 'A', 'successor': ['C', 'D']},
    'C': {'predecessor': 'B', 'successor': ['E']},
    'D': {'predecessor': 'B', 'successor': ['F']},
    'E': {'predecessor': 'C', 'successor': None},
    'F': {'predecessor': 'D', 'successor': None}
}

nodes_fig3 = {
    'A': {'predecessor': None, 'successor': ['B']},
    'B': {'predecessor': 'A', 'successor': ['C', 'D']},
    'C': {'predecessor': 'B', 'successor': ['D']},
    'D': {'predecessor': 'B', 'successor': ['E']},
    'E': {'predecessor': ['D'], 'successor': None}
}

nodes_fig4 = {
    'A': {'predecessor': None, 'successor': ['B', 'F']},
    'B': {'predecessor': 'A', 'successor': ['C']},
    'C': {'predecessor': 'B', 'successor': ['D']},
    'D': {'predecessor': 'C', 'successor': ['E']},
    'E': {'predecessor': ['D', 'F'], 'successor': None},
    'F': {'predecessor': 'A', 'successor': ['E']}
}

nodes_fig5 = {
    'A': {'predecessor': None, 'successor': ['B', 'C']},
    'B': {'predecessor': 'A', 'successor': ['C']},
    'C': {'predecessor': ['B', 'A'], 'successor': ['D', 'E']},
    'D': {'predecessor': 'C', 'successor': ['F']},
    'E': {'predecessor': 'C', 'successor': ['F']},
    'F': {'predecessor': ['D', 'E'], 'successor': None},
}

nodes_fig6 = {
    'A': {'predecessor': None, 'successor': ['B', 'C']},
    'B': {'predecessor': 'A', 'successor': 'D'},
    'C': {'predecessor': 'A', 'successor': 'E'},
    'D': {'predecessor': ['B', 'C'], 'successor': 'H'},
    'E': {'predecessor': None, 'successor': ['F', 'G']},
    'F': {'predecessor': 'E', 'successor': 'G'},
    'G': {'predecessor': ['F', 'E'], 'successor': 'H'},
    'H': {'predecessor': ['D', 'G'], 'successor': None}
}

nodes_fig7 = {
    'X': {'predecessor': None, 'successor': ['A', 'Y']},
    'A': {'predecessor': 'X', 'successor': ['B', 'C']},
    'B': {'predecessor': 'A', 'successor': 'C'},
    'C': {'predecessor': ['A', 'B'], 'successor': 'Z'},
    'Z': {'predecessor': ['C', 'Y'], 'successor': 'E'},
    'Y': {'predecessor': 'X', 'successor': 'Z'},
    'E': {'predecessor': 'Z', 'successor': None}
}

# Define the figures dictionary with updated nodes
figs = {
    1: add_key_property(nodes_fig1, 1),
    2: add_key_property(nodes_fig2, 2),
    3: add_key_property(nodes_fig3, 3),
    4: add_key_property(nodes_fig4, 4),
    5: add_key_property(nodes_fig5, 5),
    6: add_key_property(nodes_fig6, 6),
    7: add_key_property(nodes_fig7, 7),
}

# Print the outputs
for i in range(1, len(figs) + 1):
    print(f"Nodes in Fig {i} with 'key' property added where necessary:")
    for k, v in figs[i].items():
        print(f"{k}: {v}")
    print("\n")

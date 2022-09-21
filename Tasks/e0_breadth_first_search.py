from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    print(g, start_node)
    q = Queue()
    node = start_node
    path = []

    while True:
        if node not in path:
            path.append(node)
            for neig in g.neigbours(node):
                if neig not in path and neig not in q.data:
                    q.enqueue(neig)

        node = q.enqueue()
        if node is None:
            return path

    return list(g.nodes)


if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    print(bfs(graph))
import itertools


def dijkstra(nodes: list, edges: dict, source_index: int = 0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[nodes[source_index]] = 0

    adjacent = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent[u][v] = w_uv
        adjacent[v][u] = w_uv

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)

        for v, w_uv in adjacent[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)

    return path_lengths


def GraphChallenge(strArr):
    nodes_count = int(strArr[0])

    nodes = strArr[1: nodes_count + 1]
    edges_list = strArr[nodes_count + 1:]

    edges = dict()

    for edge_list in edges_list:
        s = edge_list.split('-')[0]
        d = edge_list.split('-')[1]
        edges[(s, d)] = 1.0

    shortest_paths = dijkstra(nodes, edges)
    print(shortest_paths)
    shortest_path = shortest_paths[nodes[-1]]

    app = itertools.permutations(nodes, int(shortest_path) + 1)

    best_possible_paths = list()
    for p in app:
        shortest_paths = dijkstra(nodes, edges)
        if nodes[0] == p[0] and nodes[-1] == p[-1]:
            success = 0
            for node in p[1:]:

                if shortest_paths[node] == 1.0:
                    success += 1
                else:
                    break

                shortest_paths = dijkstra(nodes, edges, nodes.index(node))

                if success == int(shortest_path):
                    best_possible_paths.append(p)

    return -1 if not best_possible_paths else '-'.join(best_possible_paths[0])


if __name__ == '__main__':
    # keep this function call here
    print(
        GraphChallenge(["4","X","Y","Z","W","X-Y","Y-Z","X-W"]))

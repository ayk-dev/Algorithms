from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    q = deque([node])
    visited.add(node)

    while q:
        current_node = q.popleft()
        print(current_node, end=' ')

        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                q.append(child)


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: []
}

visited = set()


for node in graph:
    bfs(node, graph, visited)
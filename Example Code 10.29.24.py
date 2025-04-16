graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

matrix = [[0, 1, 1, 0], 
          [1, 0, 0, 1], 
          [1, 0, 0, 1], 
          [0, 1, 1, 0]]

def dfs(graph: dict, node: int, visited: set):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

from collections import deque
def bfs(graph: dict, start: int):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

import heapq
def prim_mst(graph):
    mst_weight = 0
    visited = set()
    min_heap = [(0, 0)] # (cost, start node)

    while len(visited) < len(graph):
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_weight += cost
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
    return mst_weight



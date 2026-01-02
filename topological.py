from collections import defaultdict
from typing import List

def topological(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    visited = [False] * n
    stack = []

    def dfs(node):
        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)
        stack.append(node)
    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return graph[curr][neighbor] * res

            return -1.0

        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(a, b, set()))

        return results

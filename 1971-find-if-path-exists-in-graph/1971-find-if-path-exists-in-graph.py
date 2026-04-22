class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , validate):
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in validate:
                    found = dfs(neighbor , validate)
                    if found:
                        return True

            return False

        visited = set()
        return dfs(source , visited)
            

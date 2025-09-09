from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_cyclic(self):
        visited = [False] * self.V

        def dfs(node, parent):
            visited[node] = True
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for i in range(self.V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False

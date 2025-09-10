from collections import deque, defaultdict

def shortest_path(V, edges, start, end):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    dist = [-1] * V
    dist[start] = 0

    q = deque([start])

    while q:
        node = q.popleft()
        
        if node == end:
            return dist[node]

        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    return -1

n = 5 #--> number of nodes
# n, m = map(int, input().split()) --> Number of nodes and edges are taken in inputs
graph = [[0]*n for _ in range(n)]

# edges given
edges = [(0, 1), (0, 2), (1, 3)]


for u,v in edges:
    #  u, v = map(int, input().split()) --> (node,edge) pair as input
    graph[u][v]=1
    graph[v][u]=1 #--> for undirected

for row in graph:
    print(row)

n = 5 #--> number of nodes
# n, m = map(int, input().split()) --> Number of nodes and edges are taken in inputs
alist = [[] for _ in range(n)]

# edges given
edges = [(0, 1), (0, 2), (1, 3)]

for u,v in edges:
    #  u, v = map(int, input().split()) --> (node,edge) pair as input
    alist[u].append(v)
    alist[v].append(u) #--> undirected


for i in range(n):
    print(i, ":", alist[i])

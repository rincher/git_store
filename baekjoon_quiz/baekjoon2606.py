import sys
total = int(sys.stdin.readline())
computers = int(sys.stdin.readline())
connected_computers = {}

for i in range(1, total+1):
    connected_computers[i] = set()

for j in range(1, computers+1):
    a, b = map(int, sys.stdin.readline().split())
    connected_computers[a].add(b)
    connected_computers[b].add(a)


def dfs_stack(adjacent_graph, start_node):
    visited = []
    for i in connected_computers[start_node]:
        if i not in visited:
            visited.append(i)
            dfs_stack(connected_computers, i)


dfs_stack(connected_computers, 1)
print(len(visited)-1)

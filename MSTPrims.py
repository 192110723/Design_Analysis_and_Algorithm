INF = 9999999
V = 5
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [False] * V
selected[0] = True
no_edge, total_cost = 0, 0

print("Edge : Weight\n")

while no_edge < V - 1:
    minimum = INF
    x, y = 0, 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j] and minimum > G[i][j]:
                    minimum, x, y = G[i][j], i, j

    print(f"{x}-{y}:{G[x][y]}")
    total_cost += G[x][y]
    selected[y] = True
    no_edge += 1

print("Total Cost of Minimum Spanning Tree:", total_cost)

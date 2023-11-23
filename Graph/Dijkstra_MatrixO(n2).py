import sys


def Matrix_graph(n):
  # n*n 矩阵表示
  graph = [[0 for _ in range(n + 10)] for i in range(n + 10)]
  for i in range(1, n + 1):
    tmp = map(int, sys.stdin.readline().split())
    for j, w in enumerate(tmp):
      graph[i][j + 1] = w
  return graph


def vector_graph(n, m):
  # 链式前向星存m条边
  graph = [{} for _ in range(n + 10)]
  for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w
    graph[v][u] = w
  return graph


def Dijkstra_Matrix(dis, graph, st, ed):
  dis[st] = 0
  vis = set()

  for cnt in range(n):
    min_val = sys.maxsize
    x = -1
    for i in range(1, n + 1):
      if i not in vis and dis[i] < min_val:
        min_val = dis[i]
        x = i
    vis.add(x)
    for y in range(1, n + 1):
      dis[y] = min(dis[y], dis[x] + graph[x][y])


if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().split())
  graph = [[0 if _ == i else sys.maxsize for _ in range(n + 10)] for i in range(n + 10)]
  for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = min(graph[u][v], w)

  dis = [sys.maxsize for _ in range(n + 10)]
  st, ed = 1, n

  Dijkstra_Matrix(dis, graph, st, ed)
  print(-1 if dis[ed] > sys.maxsize / 2 else dis[ed])
  pass

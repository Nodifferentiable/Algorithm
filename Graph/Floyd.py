'''
第一行包含三个整数 n,m,k
接下来 m行，每行包含三个整数 x,y,z
表示存在一条从点 x到点 y的有向边，边长为 z
接下来 k行，每行包含两个整数 x,y
表示询问点 x到点 y的最短距离。
'''
import sys


def Floyd(dist):
  for k in range(1, n + 1):
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == "__main__":
  n, m, k = map(int, sys.stdin.readline().split())
  graph = [[0 if _ == i else sys.maxsize for _ in range(n + 10)] for i in range(n + 10)]
  for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = min(graph[u][v], w)

  Floyd(graph)

  for i in range(k):
    u, v = map(int, sys.stdin.readline().split())
    print("impossible" if graph[u][v] > sys.maxsize / 2 else graph[u][v])
  pass

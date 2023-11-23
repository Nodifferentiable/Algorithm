import sys
import collections

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
    graph = [[sys.maxsize for i in range(n + 1)] for j in range(n + 1)]

    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())

        graph[u][v] =graph[v][u] = min(graph[u][v], w)

    for i in range(1, n + 1):
        graph[i][i] = 0
    return graph


def Prim_vector(dis, graph):
    vis = set()
    dis[1] = 0
    res = 0

    for i in range(n):  # n次
        t = 0
        for j in range(1, n + 1):
            if j not in vis and (t == -1 or dis[t] > dis[j]):
                t = j
        if dis[t] == sys.maxsize:
            return sys.maxsize

        res += dis[t]
        vis.add(t)

        for j in range(1, n + 1):
            dis[j] = min(dis[j], graph[t][j])

    return res


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = vector_graph(n, m)
    dis = [sys.maxsize for _ in range(n + 10)]
    ans = Prim_vector(dis, graph=graph)
    print("impossible" if ans > sys.maxsize / 2 else ans)
    pass

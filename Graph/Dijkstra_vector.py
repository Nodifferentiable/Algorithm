import queue
import sys
#也可以用heapq collections.defaultdict


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
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w
    return graph


def Dijkstra_vector(dis, graph, st, ed):
    dis[st] = 0
    vis = set()
    q = queue.PriorityQueue()
    q.put((0, st))

    while not q.empty():
        d, t = q.get()
        if t in vis:
            continue
        vis.add(t)

        for v, w in graph[t].items():
            if dis[v] > dis[t] + w:
                dis[v] = dis[t] + w
                q.put((dis[v], v))


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    graph = vector_graph(n, m)

    dis = [sys.maxsize for _ in range(n + 10)]
    st, ed = 1, n

    Dijkstra_vector(dis, graph, st, ed)
    print(-1 if dis[ed] > sys.maxsize / 2 else dis[ed])
    pass

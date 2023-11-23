import sys
import collections


def DFS(u):
    for v in graph[u]: #当前点连接的其他点
        if v not in vis:
            vis.add(v)
            if linker[v] == -1 or DFS(linker[v]):
                linker[v] = u
                return True
    return False


if __name__ == "__main__":
    n1, n2, m = map(int, sys.stdin.readline().split())

    graph = collections.defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    res = 0
    vis = set()
    linker = [-1 for i in range(max(n1, n2) + 10)]

    for i in range(1,n1+1):
        vis.clear()
        if DFS(i): res += 1

    print(res)
    pass

import sys
import collections


def Find(x):
    if p[x] != x:
        p[x] = Find(p[x])
    return p[x]


def Kruskal(edge):
    res, cnt = 0, 0
    for u, v, w in edge:
        u = Find(u)
        v = Find(v)
        if u != v:
            res += w
            p[u] = v
            cnt += 1
    return cnt, res


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    # 排序
    edge = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(m)], key=lambda x: x[-1])
    p = list(range(n + 10))  # fa array
    cnt, ans = Kruskal(edge)
    print("impossible" if cnt != n - 1 else ans)
    pass

import sys

if __name__ == "__main__":
  n = int(sys.stdin.readline().split()[0])

  data = sorted([tuple(map(str, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (int(x[-1]),int(x[0])),
                reverse=False)
  [print(d[0], d[1], sep=' ') for d in data]
  pass

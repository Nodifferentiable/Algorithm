import sys

if __name__ == "__main__":
  try:
    while True:
      n = int(sys.stdin.readline().split()[0])
      print(str(bin(n))[2:])
  except:
    pass

  pass

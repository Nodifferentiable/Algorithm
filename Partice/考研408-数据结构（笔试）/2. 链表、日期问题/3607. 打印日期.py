import sys
import itertools
import datetime

if __name__ == "__main__":
  try:
    while True:
      y, d = map(int, sys.stdin.readline().split())
      dt=datetime.datetime(y,1,1)
      dt+=datetime.timedelta(days=d-1)
      print("{:04d}-{:02d}-{:02d}".format(dt.year,dt.month,dt.day))
  except:
    pass

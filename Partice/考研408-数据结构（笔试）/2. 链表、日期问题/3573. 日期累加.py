dic = {'+': 1, '-': 1, '*': 2, '/': 2}

s = input()

i = 0
num = []
op = []


def eval():
  b = num.pop()
  a = num.pop()
  c = op.pop()
  if c == '+':
    x = a + b
  elif c == '-':
    x = a - b
  elif c == '*':
    x = a * b
  else:
    x = int(a / b)
  num.append(x)


while i < len(s):
  if s[i].isdigit():
    j = i
    x = 0
    while j < len(s) and s[j].isdigit():
      x = x * 10 + int(s[j])
      j += 1
    num.append(x)
    i = j - 1
  elif s[i] == '(':
    op.append(s[i])
  elif s[i] == ')':
    while op[-1] != '(':
      eval()
    op.pop()
  else:
    while len(op) and op[-1] != '(' and dic[op[-1]] >= dic[s[i]]:
      eval()
    op.append(s[i])
  i += 1

while op:
  eval()
print(num[0])

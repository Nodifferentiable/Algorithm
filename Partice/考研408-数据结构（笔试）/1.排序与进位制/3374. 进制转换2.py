def base_conversion(x, M, N):
  valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 有效的 M 进制字符

  decimal_num = 0
  for i, digit in enumerate(reversed(x)):
    if digit not in valid_chars[:M]:  # 检查输入字符是否在 M 进制范围内
      raise ValueError("Invalid input character")
    decimal_num += valid_chars.index(digit) * (M ** i)

  result = ''
  while decimal_num > 0:
    remain = decimal_num % N
    if remain >= 10:
      result += chr(ord('a') + remain - 10)
    else:
      result += valid_chars[remain]
    decimal_num //= N

  return result[::-1]


if __name__ == "__main__":
  try:
    while True:
      line = input()
      if not line:
        break
      M, N = map(int, line.split())
      x = input().strip()
      print(base_conversion(x, M, N))
  except EOFError:
    pass

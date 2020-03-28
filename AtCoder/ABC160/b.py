x = int(input())
coins = [500, 5]
joy = 0
for coin in coins:
  val = x // coin
  x = x % coin
  if coin == 500:
    joy += val * 1000
  elif coin == 5:
    joy += val * 5
print(joy)
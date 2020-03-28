X, Y, A, B, C = map(int, input().split(' '))
p = list(map(int, input().split(' ')))
q = list(map(int, input().split(' ')))
r = list(map(int, input().split(' ')))

p.sort()
q.sort()
r.sort()

pi = A - 1
qi = B - 1
ri = C - 1

yummy = 0
i = 1
while i <= X + Y:
  if pi > A - X - 1 and qi > B - Y - 1:
    a = p[pi]
    b = q[qi]
    c = r[ri]
    if c < a and c < b:
      yummy += a + b
      pi -= 1
      qi -= 1
      i += 2
    else:
      if a < b:
        yummy += c + b
        qi -= 1
        ri -= 1
        i += 2
      else:
        yummy += a + c
        pi -= 1
        ri -= 1
        i += 2
  elif pi > A - X - 1:
    a = p[pi]
    c = r[ri]
    if a < c:
      yummy += c
      ri -= 1
      i += 1
    else:
      yummy += a
      pi -= 1
      i += 1
  elif qi > B - Y - 1:
    b = q[qi]
    c = r[ri]
    if b < c:
      yummy += c
      ri -= 1
      i += 1
    else:
      yummy += b
      qi -= 1
      i += 1

print(yummy)
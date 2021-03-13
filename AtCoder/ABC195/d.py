import copy

def find_max_index(w, left_items):
  ok_items = list(filter(lambda item: item[0] <= w, left_items))
  if len(ok_items) > 0:
    max_value = max(ok_items, key=lambda item: item[1])
    max_index = left_items.index(max_value)
    return max_index
  else:
    return None

N, M, Q = map(int, input().split(' '))
items = [None for n in range(N)]
for n in range(N):
  items[n] = list(map(int, input().split(' ')))
X = list(map(int, input().split(' ')))
query = [None for q in range(Q)] # query[0] = L, query[1] = R
for q in range(Q):
  query[q] = list(map(int, input().split(' ')))

for q in query:
  available_boxes = X[:q[0]-1] + X[q[1]:]
  available_boxes.sort()
  left_items = copy.deepcopy(items)
  sum_value = 0
  for box in available_boxes:
    max_index = find_max_index(box, left_items)
    if max_index != None:
      sum_value += left_items.pop(max_index)[1]
      available_boxes.remove(box)
    else:
      break
  print(sum_value)

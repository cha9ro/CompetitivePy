import copy

n = int(input())
line = input().split(' ')
x = []
xSorted = []
for element in line:
    x.append(int(element))
    xSorted.append(int(element))
xSorted.sort()

originalMedian = xSorted[int(n/2)-1]

for element in x:
    if element >= originalMedian:
        print (xSorted[int(n/2)-1])
    else:
        print (xSorted[int(n/2)+1])

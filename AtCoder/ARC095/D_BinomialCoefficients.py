n = int(input())
line = input().split(' ')
a = [int(x) for x in line]

maxVal = max(a)
closestVal = a[0]
for x in a:
    if abs(x-maxVal/2) < abs(closestVal-maxVal/2):
        closestVal = x

print (maxVal, closestVal)
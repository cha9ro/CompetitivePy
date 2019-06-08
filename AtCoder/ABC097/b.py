import math
X = int(input())
x = int(math.sqrt(X))
maxVal = x
for i in range(2, x+1):
    val = i
    while val <= X:
        val *= i
    val = int(val/i)
    if val > maxVal:
        maxVal = val
print (maxVal)
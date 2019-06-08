def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    if n<r:
        print (0)
        exit()
    return int(factorial(n)/factorial(n-r)/factorial(r))

N = int(input())
names = []
count = [0] * 5
overlap3 = [0] * 5
overlap2 = [0] * 5

for i in range(N):
    names.append(input())
    if names[i][0] == 'M':
        count[0] += 1
    elif names[i][0] == 'A':
        count[1] += 1
    elif names[i][0] == 'R':
        count[2] += 1
    elif names[i][0] == 'C':
        count[3] += 1
    elif names[i][0] == 'H':
        count[4] += 1

if sum(count)<3:
    print (0)
    exit()

for i in range(5):
    if count[i] > 2:
        overlap3[i] = combination(count[i], 3)
    if count[i] == 2:
        overlap2[i] = combination(count[i], 2)

out = combination(sum(count),3) - sum(overlap2)*(sum(count)-2) - sum(overlap3)

"""
print ('1: ', combination(sum(count),3))
print ('2: ', sum(overlap2)*(sum(count)-2))
print ('3: ', sum(overlap3))
"""

if out > 0:
    print (out)
else:
    print (0)

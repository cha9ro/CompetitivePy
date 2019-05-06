import math

def isInRange(x, y, t, d, r, a, b):
    cam2WorkDegree = math.degrees(math.atan2(b-y, a-x))
    if cam2WorkDegree < 0:
        cam2WorkDegree += 360
    cam2WorkDistance = math.sqrt((b-y)*(b-y) + (a-x)*(a-x))
    if float(t - d/2) <= cam2WorkDegree and cam2WorkDegree <= float(t + d/2) and cam2WorkDistance <= r:
        return True
    else:
        return False


# read parameters
line = input().split(' ')
W = int(line[0])
H = int(line[1])
M = int(line[2])
N = int(line[3])

# read camera info
x = [0 for m in range(M)]
y = [0 for m in range(M)]
t = [0 for m in range(M)]
d = [0 for m in range(M)]
r = [0 for m in range(M)]

for m in range(M):
    line = input().split(' ')
    x[m] = int(line[0])
    y[m] = int(line[1])
    t[m] = int(line[2])
    d[m] = int(line[3])
    r[m] = int(line[4])

# read work info
a = [0 for n in range(N)]
b = [0 for n in range(N)]

for n in range(N):
    line = input().split(' ')
    a[n] = int(line[0])
    b[n] = int(line[1])

for n in range(N):
    isOK = False
    for m in range(M):
        if isInRange(x[m], y[m], t[m], d[m], r[m], a[n], b[n]):
            isOK = True
            break
    if isOK:
        print ('yes')
    else:
        print('no')




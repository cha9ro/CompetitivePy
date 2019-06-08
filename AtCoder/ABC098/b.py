n = int(input())
s = input()

output = 0
for i, pivot in enumerate(s):
    x = s[:i]
    y = s[i:]
    dic = {}
    out = 0
    for c in x:
        if not c in dic:
            dic[c] = 1
    for c in y:
        if c in dic:
            out += 1
            del dic[c]
    if out > output:
        output = out

print (output)
n = input()
s = input()
isFour = False
for c in s:
    if c == 'Y':
        print ('Four')
        isFour = True
        break

if not isFour:
    print ('Three')

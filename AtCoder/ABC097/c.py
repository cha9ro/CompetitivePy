s = input()
K = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
k = 0
isFound = False

# return True if stays in the same head, else return False
def getSubstr(charStack, l):
    global k
    strStack = []
    while charStack != []:
        head = charStack.pop()
        if head + l <= len(s):
            strStack.append(s[head:head+l])
    
    print(strStack)
    # if no sub-string is found
    if strStack == []:
        return False, False, None
    
    strStack.sort()
    table = {}
    for item in strStack:
        if item in table:
            strStack.remove(item)
        else:
            table[item] = 1
    print(strStack)

    while k <= K and strStack != []:
        k += 1
        out = strStack.pop()
    if k == K:
        isFound = True
    else:
        isFound = False
    return True, isFound, out

    

for targetChar in alphabet:
    isFound = False
    out = None
    if isFound:
        print (out)
        break
    charStack = []
    for i, c in enumerate(s):
        if c == targetChar:
            charStack.append(i)
    print(charStack)
    if len(charStack) > 0:
        k += 1
    l = 1
    isStay = True
    while isStay:
        isStay, isFound, out = getSubstr(charStack, l)
        if isStay:
            print ('--------')
            l += 1
        else:
            break


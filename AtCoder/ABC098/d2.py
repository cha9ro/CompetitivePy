def isXorSum(array):
    # print('input:', array)
    xor = array[0]
    if len(array) > 1:
        for i in range(1,len(array)):
            xor = xor ^ array[i]
    if xor == sum(array):
        # print('okay:',array)
        return True
    else:
        return False

N = int(input())
A = input().split(' ')
A = [int(val) for val in A]
out = 0
for l in range(len(A)):
    for r in range(l+1, len(A)+1):
        if isXorSum(A[l:r]):
            out += 1
        else:
            break
print (out)


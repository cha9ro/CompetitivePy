def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    return int(factorial(n)/factorial(n-r)/factorial(r))

n = int(input())
print (factorial(n))
r = int(input())
print (combination(n,r))
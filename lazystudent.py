from math import factorial,ceil
def ncr(n,r):
    return((factorial(n))/(factorial(n-r)*factorial(r)))
t=int(input())
for i in range(t):
    N,T,M=map(int,input().split())
    p=ncr(N-M,T)
    q=ncr(N,T)
    a=1-(p/q)
    b=1000000007
    print(ceil(a*b))


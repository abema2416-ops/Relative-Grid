import itertools, math
from functools import lru_cache
def isprime(n): return n>1 and all(n%p for p in range(2,int(n**.5)+1))
def pf(n):
    r=[];p=2
    while p*p<=n:
        while n%p==0:r.append(p);n//=p
        p+=1
    if n>1:r.append(n)
    return r
def gen(M):  # all products of sub-multisets
    s={1}
    for f in M: s|={x*f for x in s}
    return s
def rmin(H,maxf=None):
    H=[h for h in set(H) if h>1]
    if not H:return 0
    cands=sorted({d for h in H for d in range(2,h+1) if h%d==0})
    for k in range(1,8):
        for M in itertools.combinations_with_replacement(cands,k):
            if all(h in gen(M) for h in H):return k
def rule(H):  # user's rule: prime ->1; composite -> 0 if all its prime factors are among heights, else 1
    H=set(h for h in H if h>1);c=0
    for h in H:
        if isprime(h):c+=1
        else:c+= 0 if all(p in H for p in set(pf(h))) else 1
    return c
tests=[{3,6,2},{2,3,4},{2,4},{2,3,12},{6},{2,6},{6,10,15},{6,10,15,30},{2,3,5,30},{4,8},{2,3,6,9},{5,7},{2,3,4,5,6}]
for H in tests:print(sorted(H),'R_min=',rmin(H),' rule=',rule(H),' log2>=',math.ceil(math.log2(len(H|{1}))))

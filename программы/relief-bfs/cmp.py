import itertools,sys
from functools import lru_cache
def R(H):
    H=sorted(set(h for h in H if h>1))
    if not H: return 0
    M=max(H)
    for r in range(1,len(H)+1):
        for fs in itertools.combinations_with_replacement(range(2,M+1),r):
            prods=set()
            for k in range(1,r+1):
                for sub in itertools.combinations(fs,k):
                    p=1
                    for x in sub: p*=x
                    prods.add(p)
            if all(h in prods for h in H): return r
    return len(H)
W,Hmax,D=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
found={}
for line in open(sys.argv[4]):
    a,b=line.split(':'); found[tuple(map(int,a.split()))]=int(b)
below=[];missing=[]
for h in itertools.product(range(1,Hmax+1),repeat=W):
    col=1+R(h) if W>1 else R(h)
    if all(x==1 for x in h): col=1
    l=found.get(h)
    if l is not None and l<col: below.append((h,l,col))
    if l is None and col<=D: missing.append((h,col))
print("reliefs:",Hmax**W,"found<=D:",len(found))
print("l < 1+R:",len(below)); print(below[:15])
print("column bound <=D but not reached:",len(missing)); print(missing[:15])

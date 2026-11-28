import json, math, time
from collections import Counter
import sys; sys.path.insert(0,'.')
from gcd_kent import cover
def nf(n):
    c=0;p=2
    while p*p<=n:
        while n%p==0: n//=p; c+=1
        p+=1
    return c+(n>1)
def gcd_kent2(H,score):
    H=sorted(set(H)); chosen=[]; rest={h:h for h in H}
    while True:
        todo=[r for r in rest.values() if r>1]
        if not todo: break
        C=Counter()
        for i in range(len(todo)):
            for j in range(i+1,len(todo)):
                g=math.gcd(todo[i],todo[j])
                if g>1: C[g]+=1
        # кусок должен ровно «вырезаться» хотя бы из двух остатков
        best=None
        for g,c in C.items():
            uses=sum(1 for r in todo if r%g==0 and math.gcd(g,r//g)==1)
            if uses<2: continue
            s=score(uses,nf(g))
            if best is None or s>best[0]: best=(s,g)
        if not best: chosen+=list(set(todo)); break
        g=best[1]; chosen.append(g)
        for h in rest:
            if rest[h]%g==0 and math.gcd(g,rest[h]//g)==1: rest[h]//=g
    chosen=sorted(set(chosen)); return chosen, all(cover(h,chosen) for h in H)
d=json.load(open('hell.json')); H=d['H']; secret=set(d['M_secret'])
for name,sc in [("частота × размер",lambda u,k:u*k),("экономия (частота−1)×(размер−1)",lambda u,k:(u-1)*(k-1)),("сначала крупные",lambda u,k:(k,u)),("частота, потом размер",lambda u,k:(u,k))]:
    t=time.time(); M,ok=gcd_kent2(H,sc)
    print(f"{name:32s}: множителей {len(M)}, собирают все: {ok}, тайных угадано {len(set(M)&secret)}/60, {time.time()-t:.1f} с",flush=True)

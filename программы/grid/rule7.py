from lib import *
exec(open('rule6.py').read().split('random.seed')[0].replace('from lib import *',''))
def rule7(H):
    # user's local rule: a common factor g is taken when its leftovers (height / g) repeat
    # or are themselves heights/taken multipliers; otherwise heights are raised separately
    need=set(h for h in H if h>1);M=[];covered=set()
    while True:
        best=None
        for g in range(2,max(need|{2})+1):
            S=[v for v in need-covered if v%g==0 and v!=g]
            if len(S)<1:continue
            Q=[v//g for v in S]
            newq={q for q in Q if q>1 and q not in need and q not in gen(M)}
            cost=1+len(newq)-(1 if g in need and g not in gen(M) else 0)
            gain=len(S)-cost
            if gain>0 and (best is None or gain>best[0]):best=(gain,g,S,Q)
        if not best:break
        _,g,S,Q=best;M.append(g);covered|=set(S)
        for q in set(Q):
            if q>1 and q not in gen(M):M.append(q)
    for v in sorted(need):
        if v not in gen(M):M.append(v)
    # sanity: construction valid
    assert all(h in gen(M) for h in need)
    return len(M)
random.seed(1);N=1000;e=un=0;ex=[]
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a=rmin(H);m=min(rule3(H),primes_rule(H),rule7(H));r7=rule7(H)
    e+=(m==a);un+=(r7<a)
    if m!=a:ex.append((sorted(H),a,rule3(H),primes_rule(H),r7))
print('best-of-three exact',e,'under',un);print(ex[:6])
random.seed(1);print('rule7 alone exact',sum(rule7(H)==rmin(H) for H in [set(random.sample(range(2,41),random.randint(2,6))) for _ in range(1000)]))

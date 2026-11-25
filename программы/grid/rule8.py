from lib import *
def common_divs(H):
    H=[h for h in set(H) if h>1]
    C=set(H)
    for d in range(2,max(H)+1):
        if sum(1 for h in H if h%d==0)>=2:C.add(d)
    for h in H:
        for d in list(C):
            if h%d==0 and h//d>1:C.add(h//d)
    return sorted(C)
def rmin_restricted(H):
    H=[h for h in set(H) if h>1];C=common_divs(H)
    for k in range(1,9):
        for M in itertools.combinations_with_replacement(C,k):
            if all(h in gen(M) for h in H):return k
def greedy(H):
    # user's idea: divisors shared by several heights first (by how many heights they divide), then old rules
    H=[h for h in set(H) if h>1];M=[]
    rem={h:h for h in H}
    while True:
        best=None
        for d in range(2,max(H)+1):
            S=[h for h in H if rem[h]%d==0 and rem[h]>1]
            if len(S)<2:continue
            # quotient leftovers after taking d
            Q=[rem[h]//d for h in S]
            newq=len({q for q in Q if q>1 and q not in [rem[x] for x in H if x not in S]})
            gain=len(S)-1-newq+sum(1 for q in Q if q==1)   # heights finished outright count extra
            key=(gain,len(S),d)
            if best is None or key>best[0]:best=(key,d,S)
        if not best or best[0][0]<=0:break
        _,d,S=best;M.append(d)
        for h in S:rem[h]//=d
    for v in sorted(set(r for r in rem.values() if r>1)):   # leftovers: smaller first, separately (old rule)
        if not all((h in gen(M)) for h in H):
            if v not in gen(M):M.append(v)
    for h in sorted(H):
        if h not in gen(M):M.append(h)
    assert all(h in gen(M) for h in H)
    return len(M)
random.seed(1);N=1000;ex=0;eg=0;eb=0;un=0;bad=[]
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a=rmin(H);b=rmin_restricted(H);g=greedy(H);r=rule3(H)
    ex+=(a==b);eg+=(g==a);eb+=(min(g,r)==a);un+=(g<a)
    if min(g,r)!=a:bad.append((sorted(H),a,g,r))
print('restricted search exact',ex,' greedy-by-common-divisors exact',eg,' best(greedy,old)',eb,' under',un)
print(bad[:6]); print(greedy([4,6,7,8,21,24]),greedy([6,10,15,30]),greedy([30,33]))

from lib import *
def rule5(H):
    # user's rule: a common factor g is used only if its quotients repeat / are already taken,
    # i.e. 1 + (distinct new quotients) < (number of heights it covers); else heights are raised separately.
    V=sorted(set(h for h in H if h>1));M=[]
    while True:
        best=None
        for g in range(2,max(V+[2])+1):
            S=[v for v in V if v%g==0 and v!=g] + [v for v in V if v==g]
            if len(S)<2:continue
            Q=set(v//g for v in S if v//g>1)
            newq=[q for q in Q if q not in gen(M)]
            gain=len(S)-(1+len(newq))
            if gain>0 and (best is None or gain>best[0]):best=(gain,g,S)
        if not best:break
        g,S=best[1],best[2];M.append(g);V=[v for v in V if v not in S]+[v//g for v in S if v//g>1];V=sorted(set(V))
        V=[v for v in V if v not in gen(M) or v in M and False]
    for v in sorted(V):   # the rest: the user's earlier rule, smaller first
        if v not in gen(M):M.append(v)
    return len(M)
random.seed(1);N=1000;e5=e3=best=under=0
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a=rmin(H);b=rule3(H);c=rule5(H)
    e3+=(b==a);e5+=(c==a);best+=(min(b,c)==a);under+=(c<a)
print('rule3',e3,'rule5',e5,'min',best,'under',under)
for H in [{6,10,15,30},{30,33},{12,18},{2,3,6,12},{2,4}]:print(sorted(H),rmin(H),rule5(H))

import json, math, time, sys, itertools as it
from functools import lru_cache
def divisors(n):
    ds=[1]
    m=n; p=2; fac=[]
    while p*p<=m:
        if m%p==0:
            e=0
            while m%p==0: m//=p; e+=1
            fac.append((p,e))
        p+=1 if p==2 else 2
    if m>1: fac.append((m,1))
    for p,e in fac: ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def solve(H,k,deadline):
    """Точный поиск «R ≤ k?»: берём самую маленькую ещё не собранную высоту h; она — произведение части
    набора, значит следующий множитель — делитель h / p, где p — произведение уже выбранных (закономерности:
    делители, высоты, степени и повторяющиеся множители появляются тут сами). Отсечения: число непустых
    произведений из k множителей не больше 2^k − 1; каждая высота должна делиться на что-то собираемое."""
    H=sorted(set(h for h in H if h>1)); nodes=[0]
    def prods(M):
        s={1}
        for m in M: s|={x*m for x in s}
        return s
    def dfs(M):
        nodes[0]+=1
        if time.time()>deadline: raise TimeoutError
        P=prods(M); rest=[h for h in H if h not in P]
        if not rest: return list(M)
        if len(M)==k: return None
        # отсечение: оставшиеся r множителей дают не больше (2^r)·|P| − |P| новых произведений
        r=k-len(M)
        if len(rest) > (2**r-1)*len(P): return None
        h=rest[0]; seen=set()
        for p in P:
            if h%p: continue
            q=h//p
            for d in divisors(q):
                if d<2 or d in seen: continue
                seen.add(d)
                res=dfs(M+[d])
                if res: return res
        return None
    for kk in range(1,k+1):
        k=kk
        res=dfs([])
        if res: return kk,res,nodes[0]
    return None,None,nodes[0]
H=json.load(open(sys.argv[1]))[0]['H']
t=time.time()
try:
    print(solve(H,int(sys.argv[2]),t+float(sys.argv[3])),'за',round(time.time()-t,1),'с')
except TimeoutError: print('не успел за',sys.argv[3],'с')

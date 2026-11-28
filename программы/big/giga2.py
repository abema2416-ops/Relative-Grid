"""Гигакент-2: график как главный инструмент.
1) низ = max(ранг, ⌈log₂(D+1)⌉);  2) кент скачков;  3) суперкент, ведомый графиком (делители
перебираются в порядке частоты скачков);  4) запасной верх — число высот. Ответ точный, когда верх = низ."""
import json, math, time, itertools, random, sys
from collections import Counter
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
from superkent import divisors
from jumps import jumps, builds
def guided(H,kmax,deadline,kmin,freq):
    H=sorted(set(h for h in H if h>1)); nodes=[0]
    def prods(M):
        s={1}
        for m in M: s|={x*m for x in s}
        return s
    def dfs(M,k):
        nodes[0]+=1
        if time.time()>deadline: raise TimeoutError
        P=prods(M); rest=[h for h in H if h not in P]
        if not rest: return list(M)
        if len(M)==k: return None
        r=k-len(M)
        if len(rest)>(2**r-1)*len(P): return None
        # выбираем высоту с наименьшим числом вариантов (самая «узкая» точка графика)
        best=None
        for h in rest[:8]:
            opts=set()
            for p in P:
                if h%p==0: opts|={d for d in divisors(h//p) if d>1}
            if best is None or len(opts)<len(best[1]): best=(h,opts)
        for d in sorted(best[1],key=lambda d:(-freq.get(d,0),d)):
            res=dfs(M+[d],k)
            if res: return res
        return None
    for k in range(kmin,kmax+1):
        res=dfs([],k)
        if res: return k,res
    return None
def giga2(H,limit=60):
    H=sorted(set(h for h in H if h>1)); t=time.time()
    lb=max(rank(H),math.ceil(math.log2(len(H)+1))); ub=len(H); how='верх = число высот'
    r=jumps(H,lb,3,time.time()+min(5,limit))
    if r and r[0]<ub: ub=r[0]; how='кент скачков'
    if ub==lb: return lb,lb,ub,how+' = низ',time.time()-t
    freq=Counter(b//a for a in H for b in H if b>a and b%a==0)
    try:
        g=guided(H,ub-1,t+limit,lb,freq)
        if g: return g[0],lb,g[0],'суперкент по графику',time.time()-t
        return ub,lb,ub,'доказано: верх точный',time.time()-t
    except TimeoutError:
        return None,lb,ub,'вилка',time.time()-t
if __name__=="__main__":
    exec(open('giga_fast.py').read().split('if __name__=="__main__"')[0].split("exec(open('rank_bound.py')")[0])
    src=open('pipe.py').read().split('if __name__')[0]; exec(src)
    for name,f in [('ГИГАБОСС','boss.json'),('контрпример','fails_7.json')]:
        d=json.load(open(f)); d=d if isinstance(d,dict) else d[0]; r=giga2(d['H'])
        print(f"{name}: ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.2f} с)",flush=True)
    rng=random.Random(77); st={}; tot=0
    for i in range(30):
        kind=i%3
        if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng); name=f'спрятано {k}'
        elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3); name=f'спрятано {k}'
        else:
            P=[2,3,5,7,11,13,17,19,23,29,31,37]; u=rng.choice([10,12]); Hs=set()
            while len(Hs)<u:
                S=[p for p in P[:u] if rng.random()<0.4]
                if S: Hs.add(math.prod(S))
            H=sorted(Hs); name=f'перемешано {u}'
        r=giga2(H,120); tot+=r[4]; st[r[3]]=st.get(r[3],0)+1
        print(f"{i+1:2d}. {name:14s} ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.2f} с)",flush=True)
    print("ИТОГО:",st,f"время {tot:.1f} с",flush=True)

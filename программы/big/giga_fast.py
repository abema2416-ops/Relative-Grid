"""Быстрый гигакент: низ = max(ранг, log); верх = min(число высот, число простых);
суперкент идёт от низа вверх (ответ всегда точный, если успел); кенты не нужны."""
import sys, json, math, time, random
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
from superkent import solve as sk
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
def giga_fast(H,limit):
    H=sorted(set(h for h in H if h>1)); t=time.time()
    rk=rank(H); lb=max(rk,math.ceil(math.log2(len(H)+1)))
    F=[fac(h) for h in H]; sqf=all(max(f.values())==1 for f in F)
    ub=min(len(H), len({p for f in F for p in f})) if sqf else len(H)   # число простых — верх только без степеней
    if lb==ub: return lb,lb,ub,'ранг = верх',time.time()-t
    try:
        r,res,n=sk(H,ub,t+limit,kmin=lb); return r,lb,ub,('суперкент' if r else 'ошибка'),time.time()-t
    except TimeoutError: return None,lb,ub,'не успел',time.time()-t
if __name__=="__main__":
    B=json.load(open('boss.json')); r=giga_fast(B['H'],120)
    print(f"ГИГАБОСС: ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)
    rng=random.Random(77); st={}
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
        r=giga_fast(H,20); st[r[3]]=st.get(r[3],0)+1
        print(f"{i+1:2d}. {name}: высот {len(H)}, ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)
    print("ИТОГО:",st,flush=True)

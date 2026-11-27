"""Гигакент: низ = max(ранг, log); сначала суперкент ровно на низу (5 с); затем = max(ранг, ⌈log₂(D+1)⌉); верх = кенты (11 методов) + скульптор (замены);
совпали — ответ точный; нет — суперкент от низа до верха − 1, с лимитом времени."""
import sys, json, math, time, random
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
from superkent import solve as sk_solve
def giga(H,limit=20):
    H=sorted(set(h for h in H if h>1)); t=time.time()
    rk=rank(H); lb=max(rk, math.ceil(math.log2(len(H)+1)))
    # сначала быстрая попытка суперкента ровно на нижней границе: если вышло — ответ точный сразу
    try:
        r,res,n=sk_solve(H,lb,time.time()+min(5,limit),kmin=lb)
        if r: return r,lb,r,'суперкент на нижней границе',time.time()-t
    except TimeoutError: pass
    ub,_=method_v1(H)
    if ub>lb:
        try: ub=min(ub,len(improve2(H,gold_set(H))))
        except Exception: pass
    if ub==lb: return lb,lb,ub,'кенты = низ',time.time()-t
    try:
        r,res,n=sk_solve(H,ub-1,time.time()+limit,kmin=lb)
        if r: return r,lb,ub,'суперкент нашёл короче',time.time()-t
        return ub,lb,ub,'суперкент доказал: кенты точны',time.time()-t
    except TimeoutError:
        return None,lb,ub,'не доказано (вилка)',time.time()-t
if __name__=="__main__":
    if 'boss' in sys.argv:
        B=json.load(open('boss.json')); r=giga(B['H'],60)
        print(f"ГИГАБОСС: высот {len(B['H'])}, спрятано {len(B['M'])}: ответ {r[0]}, низ {r[1]}, верх {r[2]}, {r[3]}, {r[4]:.1f} с",flush=True); sys.exit()
    F=json.load(open('fails_7.json'))[0]; r=giga(F['H'],60)
    print(f"контрпример кентам: ответ {r[0]}, низ {r[1]}, верх {r[2]}, {r[3]}, {r[4]:.1f} с",flush=True)
    rng=random.Random(77); stats={}
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
        r=giga(H,20); stats[r[3]]=stats.get(r[3],0)+1
        print(f"{i+1:2d}. {name}: высот {len(H)}, ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)
    print("ИТОГО:",stats)

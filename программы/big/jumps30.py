import sys, json, math, random, time
exec(open('giga_fast.py').read().split('if __name__=="__main__"')[0])
from jumps import jumps
rng=random.Random(77); st={'точно (= граница)':0,'ответ выше границы':0,'не нашёл':0}; tot=0
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
    lb=max(rank(H),math.ceil(math.log2(len(set(H))+1)))
    t=time.time(); r=jumps(H,lb,3,time.time()+10); dt=time.time()-t; tot+=dt
    s='не нашёл' if not r else ('точно (= граница)' if r[0]==lb else 'ответ выше границы'); st[s]+=1
    print(f"{i+1:2d}. {name:14s} граница {lb:2d}, скачки: {r[0] if r else '—'}  {s}  ({dt:.2f} с)",flush=True)
print("ИТОГО:",st,f"общее время {tot:.1f} с")

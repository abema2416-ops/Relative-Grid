import sys, json, math, random, time
exec(open('giga_fast.py').read().split('if __name__=="__main__"')[0])
rng=random.Random(77); inst={}
for i in range(30):
    kind=i%3
    if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng)
    elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3)
    else:
        P=[2,3,5,7,11,13,17,19,23,29,31,37]; u=rng.choice([10,12]); Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        H=sorted(Hs)
    inst[i+1]=H
for j in [10,16,24,9,15]:
    r=giga_fast(inst[j],150)
    print(f"задача {j}: ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)

import math, random, time, sys, json, subprocess
from giga2 import giga2
P=[2,3,5,7,11,13,17,19,23,29,31]
rng=random.Random(2027); found=[]
t0=time.time()
for u in [6,7,8,9]:
    for trial in range(60):
        Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        H=sorted(Hs); r=giga2(H,5)
        if r[0] is None:
            found.append((u,H,r[1],r[2])); print(f"КОНТРПРИМЕР: простых {u}, высоты {H}, низ {r[1]}, верх {r[2]}, не решено за 5 с",flush=True)
            break
    if found and found[-1][0]==u: break
    print(f"простых {u}: 60 задач, все решены точно ({time.time()-t0:.0f} с)",flush=True)
json.dump(found,open('smallest_ce.json','w'))

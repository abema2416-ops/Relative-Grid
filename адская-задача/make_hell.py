import random, math, json, itertools
PR=[p for p in range(2,2000) if all(p%q for q in range(2,int(p**0.5)+1))]
def make(seed,u=100,k=60,D=150,bs=(3,5),per=3):
    rng=random.Random(seed); P=PR[:u]
    while True:
        B=[]
        while len(B)<k:
            b=frozenset(rng.sample(P,rng.randint(*bs)))
            if b not in B: B.append(b)
        H=set(); tries=0
        while len(H)<D and tries<200000:
            tries+=1
            c=rng.sample(range(k),per)
            if len(set().union(*[B[i] for i in c]))!=sum(len(B[i]) for i in c): continue
            H.add(frozenset(c))
        if len(H)<D: continue
        hs=[frozenset().union(*[B[i] for i in c]) for c in H]
        # нет скачков: ни одна высота не содержит другую
        if any(a<b for a in hs for b in hs): continue
        # нет одинаковых полос
        pats={tuple(p in h for h in hs) for p in P if any(p in h for h in hs)}
        used=[p for p in P if any(p in h for h in hs)]
        if len(pats)!=len(used): continue
        return [math.prod(h) for h in hs],[math.prod(b) for b in B],used
H,M,used=make(666)
json.dump({'H':sorted(H),'M_secret':sorted(M)},open('/tmp/hell/hell.json','w'))
print(f"высот {len(H)}, простых {len(used)}, спрятано множителей {len(M)}, самая длинная высота {max(len(str(h)) for h in H)} цифр")

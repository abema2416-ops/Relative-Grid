exec(open('rank_bound.py').read().split("# 1) старый")[0])
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
rng=random.Random(9)
for u in [10,12,14,16,20]:
    inst=0; fast=0; ts=[]
    for i in range(6):
        H=set()
        while len(H)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: H.add(math.prod(S))
        H=sorted(H); rk=rank(H); lb=max(rk, math.ceil(math.log2(len(H)+1))); ub=min(len(H), u)
        t=time.time()
        if lb==ub: R=lb; how='сразу (ранг = верх)'
        else:
            try: R,_,_=solve(H,ub,t+60,kmin=lb) if 'kmin' in solve.__code__.co_varnames else (None,None,None); how='поиск'
            except TimeoutError: R=None; how='поиск, не успел'
        ts.append(time.time()-t); inst+=1; fast+= R is not None
        print(f"простых {u}: ранг {rk}, верх {ub}, R = {R} ({how}, {time.time()-t:.2f} с)",flush=True)

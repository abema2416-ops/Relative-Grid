import sys, random, time, math
exec(open('/tmp/claude-0/-home-claude/70a5592c-c34c-5075-ac31-210cdddf20fb/scratchpad/superkent.py').read().split("H=json.load")[0])
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
rng=random.Random(9)
for u in [6,8,10,12,14,16,18,20]:
    ts=[];to=0;Rs=[]
    for i in range(6):
        m=u  # число высот = число простых
        H=set()
        while len(H)<m:
            S=[p for p in P[:u] if rng.random()<0.4]
            if len(S)>=1: H.add(math.prod(S))
        t=time.time()
        try:
            r,res,nodes=solve(sorted(H),len(H),t+60); ts.append(time.time()-t); Rs.append(r)
        except TimeoutError: to+=1
    print(f"простых {u}, высот {u}: решено {len(ts)}/6, среднее {sum(ts)/max(1,len(ts)):.2f} с, макс {max(ts) if ts else 0:.2f} с, R: {Rs}, не успел за 60 с: {to}",flush=True)

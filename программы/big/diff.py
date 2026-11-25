from vote import *
def diff_rule(H,top=24,cap=9):
    """author: subtract exponents between heights (= divide heights by each other) — the leftovers q = A / B
    that repeat most often are the real parts; search the smallest set among them"""
    H=sorted(set(H));Q=Counter()
    for a in H:
        for b in H:
            if a>b and a%b==0:Q[a//b]+=1
    for h in H:Q[h]+=1
    pool=sorted(Q,key=lambda q:(-Q[q],-q))[:top]
    lb=math.ceil(math.log2(len(H)+1))
    for k in range(lb,cap+1):
        for M in itertools.combinations(pool,k):
            if all(can_build(h,M) for h in H):return list(M)
    return None
if __name__=="__main__":
    rng=random.Random(2027)
    while True:
        k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
        if sorted(M)==[4,8,45,81,625,6075,8100]:break
    t=time.time();S=diff_rule(H);print('последняя тварина (7):',len(S) if S else None,sorted(S) if S else None,round(time.time()-t),'с',flush=True)
    for f in json.load(open('last3.json')):
        S=diff_rule(f['H']);print('тварина',f['k'],'->',len(S) if S else None,flush=True)
    d=json.load(open('boss.json'));t=time.time();S=diff_rule(d['H'],top=24,cap=9);print('босс 9 ->',len(S) if S else None,round(time.time()-t),'с',flush=True)

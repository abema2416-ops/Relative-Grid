from vote import *
def vote_rule2(H):
    S0,sets,V=vote_rule(H)
    core=[m for m in V if V[m]>=2 and all(m%c or m==c for c in [])]
    # residuals of every height after the agreed parts = the missing parts (author: "что остаётся свободным")
    res=Counter(h//cover(h,[m for m in V if V[m]>=2]) for h in H)
    extra=[r for r,c in res.items() if r>1 and c>=2]
    pool=sorted(set([m for m in V if V[m]>=2])|set(extra),key=lambda m:(-(V[m]+res.get(m,0)),-m))
    best=S0
    for k in range(math.ceil(math.log2(len(set(H))+1)),len(best)):
        for M in itertools.combinations(pool[:24],k):
            if all(can_build(h,M) for h in H):return list(M),pool
    return best,pool
if __name__=="__main__":
    rng=random.Random(2027)
    while True:
        k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
        if sorted(M)==[4,8,45,81,625,6075,8100]:break
    t=time.time();S,pool=vote_rule2(H);print('новая тварина, ответ 7:',len(S),sorted(S),round(time.time()-t),'с');print('пул',pool[:24])

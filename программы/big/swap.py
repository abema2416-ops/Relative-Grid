src=open('big.py').read().split('seed=int(sys.argv[1])')[0];exec(src)
def solve_set(H):
    # best rule's actual multiplier set (combo / modes style), returned as a list
    C=counts(H);best=None
    cands=[]
    G=sorted({math.gcd(a,b) for a,b in itertools.combinations(H,2)}-{1},reverse=True)
    M=list(G)
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    for key in [lambda d:d,lambda d:-d,lambda d:(C[d],d)]:
        S=prune(M,H,key)
        if best is None or len(S)<len(best):best=S
    return best
def improve(H,M):
    # author: check several methods at once — try every common part as a new component;
    # keep it if, with it, the rest can be pruned to a smaller set
    C=counts(H);cand=sorted({d for d in C if C[d]>=2}|{math.gcd(a,b) for a,b in itertools.combinations(H,2)}-{1},key=lambda d:(-C.get(d,0),-d))
    M=list(M);changed=True
    while changed:
        changed=False
        for c in cand:
            if c in M:continue
            T=prune(M+[c],H,lambda d:(d==c,C.get(d,0),d))   # never drop c first
            if len(T)<len(M):M=T;changed=True;break
    return M
for seed,idx in [(101,48),(202,9)]:
    rng=random.Random(seed)
    for i in range(idx):k=rng.choice([5,6,7]);H,Mh=make(k,rng)
    S=solve_set(H);I=improve(H,S);print(seed,idx,'было',len(S),sorted(S),'стало',len(I),sorted(I),'ответ',k)

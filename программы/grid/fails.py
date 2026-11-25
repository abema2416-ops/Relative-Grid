exec(open('allrules.py').read().split('for seed,N,hi')[0])
def best_set(H):
    H=[h for h in set(H) if h>1];cands=sorted({d for h in H for d in range(2,h+1) if h%d==0})
    for k in range(1,9):
        for M in itertools.combinations_with_replacement(cands,k):
            if all(h in gen(M) for h in H):return M
def decomp(h,M):
    for k in range(1,len(M)+1):
        for c in itertools.combinations(range(len(M)),k):
            if math.prod(M[i] for i in c)==h:return '·'.join(str(M[i]) for i in c)
out=[]
for seed,N in [(1,1000),(7,2000)]:
    random.seed(seed)
    for _ in range(N):
        H=set(random.sample(range(2,41),random.randint(2,6)))
        a=rmin(H);b=allbest(H)
        if a!=b:
            M=best_set(H);out.append((sorted(H),b,a,M,', '.join(f'{h}={decomp(h,M)}' for h in sorted(H))))
for o in out:print(o[0],'правила',o[1],'минимум',o[2],'множители',o[3],'|',o[4])
print(len(out))

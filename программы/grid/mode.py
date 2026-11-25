exec(open('freq.py').read().split('for H in [[10')[0])
def mode_rule(H,key):
    H=[h for h in set(H) if h>1];order,C=cand_order(H)
    M=[d for d in order if C[d]>=2]
    for h in sorted(H):
        if h not in gen(M):M.append(h)
    # prune: try to drop the least useful first
    for d in sorted(M,key=lambda d:key(d,C)):
        T=list(M);T.remove(d)
        if all(h in gen(T) for h in H):M=T
    return len(M)
keys={'редкие, потом мелкие':lambda d,C:(C.get(d,1),d),'редкие, потом крупные':lambda d,C:(C.get(d,1),-d),
      'крупные первыми':lambda d,C:(-d,),'мелкие первыми':lambda d,C:(d,)}
H=[4,6,7,8,21,24];print({k:mode_rule(H,f) for k,f in keys.items()})
res={k:0 for k in keys};res['all']=0;res['under']=0;bad=[]
for seed,N in [(1,1000),(7,2000)]:
    random.seed(seed)
    for _ in range(N):
        H=set(random.sample(range(2,41),random.randint(2,6)))
        a=rmin(H);vals={k:mode_rule(H,f) for k,f in keys.items()}
        for k in keys:res[k]+=vals[k]==a
        b=min(min(vals.values()),allbest(H),freq_rule(H));res['all']+=b==a;res['under']+=min(vals.values())<a
        if b!=a:bad.append((sorted(H),b,a))
print(res);print(bad)

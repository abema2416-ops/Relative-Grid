from half import *
def rule_band(H,lo,hi,indep=True):
    C=counts(H);N=len(H);cand=sorted([d for d in C if lo<=C[d]/N<=hi],key=lambda d:-d);M=[]
    for d in cand:
        if indep and any(d%m==0 or m%d==0 for m in M):continue
        M.append(d)
        if all(can_build(h,M) for h in H):break
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:(-C.get(d,0),-d))
d=json.load(open('boss.json'));H=d['H']
for lo,hi in [(0.65,0.97),(0.6,1.0),(0.7,0.96)]:
    S=rule_band(H,lo,hi);print(lo,hi,len(S),sorted(S)[:12],flush=True)

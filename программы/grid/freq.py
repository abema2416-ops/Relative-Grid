exec(open('allrules.py').read().split('for seed,N,hi')[0])
def cand_order(H):
    C={}
    for h in H:
        for d in range(2,h+1):
            if h%d==0:C[d]=C.get(d,0)+1
    return sorted(C,key=lambda d:(-C[d],-d)),C
def built(M,H):
    g=gen(M);return {h for h in H if h in g}
def freq_rule(H,need_new=True):
    H=[h for h in set(H) if h>1];order,C=cand_order(H);M=[]
    for d in order:
        if C[d]<2:break
        if need_new:
            if len(built(M+[d],H))>len(built(M,H)):M.append(d)
        else:M.append(d)
        # allow the same divisor again if it still helps (e.g. 2·2)
        while need_new and len(built(M+[d],H))>len(built(M,H)):M.append(d)
    for h in sorted(H):
        if h not in gen(M):M.append(h)
    # prune: drop multipliers not needed
    changed=True
    while changed:
        changed=False
        for i in range(len(M)):
            T=M[:i]+M[i+1:]
            if all(h in gen(T) for h in H):M=T;changed=True;break
    return len(M)
def freq_rule2(H):return freq_rule(H,False)
for H in [[10,15,20,30],[2,4,24,30,40],[4,6,7,8,21,24],[4,12,24,32,37]]:print(H,rmin(H),freq_rule(H),freq_rule2(H))
tot=0;res={'old':0,'f1':0,'f2':0,'all':0,'under':0};bad=[]
for seed,N in [(1,1000),(7,2000)]:
    random.seed(seed)
    for _ in range(N):
        H=set(random.sample(range(2,41),random.randint(2,6)))
        a=rmin(H);o=allbest(H);f1=freq_rule(H);f2=freq_rule2(H);b=min(o,f1,f2)
        res['old']+=o==a;res['f1']+=f1==a;res['f2']+=f2==a;res['all']+=b==a;res['under']+=min(f1,f2)<a;tot+=1
        if b!=a:bad.append((sorted(H),b,a))
print(tot,res);print(bad)

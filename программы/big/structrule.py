from half import *
def rule_struct(H):
    # «настоящее использование»: d засчитывается для h, только если h/d тоже есть среди высот (или h = d)
    S=set(H);C=counts(H)
    U={x:sum(1 for h in H if h%x==0 and (h//x in S or h==x)) for x in C if C[x]>=2}
    M=[]
    for x in sorted(U,key=lambda x:(-U[x],-x)):
        if all(can_build(h,M) for h in H):break
        if can_build(x,M):continue
        M.append(x)
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:(U.get(d,0),d))
if __name__=="__main__":
    d=json.load(open('boss.json'));t=time.time();S=rule_struct(d['H'])
    print('БОСС:',len(S),sorted(S),'тайные',d['M'],round(time.time()-t),'с')

from roots import *
def diff_dfs(H,top=45,cap=9,tlimit=60):
    """same author's candidates (differences of powers = quotients, frequent first), but searched smarter:
    the smallest height that cannot be built yet must use one of the chosen parts that divides it — branch on those"""
    H=sorted(set(H));Q=Counter()
    for a in H:
        for b in H:
            if a>b and a%b==0:Q[a//b]+=1
    for h in H:Q[h]+=1
    pool=sorted(Q,key=lambda q:(-Q[q],-q))[:top];rank={q:i for i,q in enumerate(pool)}
    lb=math.ceil(math.log2(len(H)+1));t0=time.time();seen=set()
    def dfs(M,k):
        if time.time()-t0>tlimit:raise TimeoutError
        un=[h for h in H if not can_build(h,M)]
        if not un:return list(M)
        if len(M)==k:return None
        key=frozenset(M)
        if key in seen:return None
        seen.add(key)
        h=un[0]
        for d in pool:
            if h%d==0 and d not in M:
                r=dfs(M+[d],k)
                if r:return r
        return None
    for k in range(lb,cap+1):
        seen.clear()
        try:
            r=dfs([],k)
        except TimeoutError:return None
        if r:return r
    return None
if __name__=="__main__":
    F=json.load(open('last2.json'))
    for M,H in F.items():
        t=time.time();S=diff_dfs(H);print('тайные',M,'->',len(S) if S else None,sorted(S) if S else None,round(time.time()-t,1),'с',flush=True)
    d=json.load(open('boss.json'));t=time.time();S=diff_dfs(d['H']);print('босс ->',len(S) if S else None,round(time.time()-t,1),'с')

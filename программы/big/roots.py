from diff import *
def iroot(n,e):
    r=round(n**(1/e))
    for x in (r-1,r,r+1):
        if x>1 and x**e==n:return x
    return None
def diff_roots_rule(H,top=26,cap=9):
    """author: differences of powers + the powers themselves: 8100 = 90^2 -> 90 and its powers are candidates too"""
    H=sorted(set(H));Q=Counter()
    for a in H:
        for b in H:
            if a>b and a%b==0:Q[a//b]+=1
    for h in H:Q[h]+=1
    base=list(Q)
    for q in base:
        for e in (2,3,4,5):
            r=iroot(q,e)
            if r:
                for j in range(1,e):Q[r**j]+=Q[q]   # the root and its lower powers
    pool=sorted(Q,key=lambda q:(-Q[q],-q))[:top]
    lb=math.ceil(math.log2(len(H)+1))
    for k in range(lb,cap+1):
        for M in itertools.combinations(pool,k):
            if all(can_build(h,M) for h in H):return list(M)
    return None
if __name__=="__main__":
    targets=[[2,9,16,20,25,2000,8100],[4,8,10,400,625,15625],[2,3,4,36,121,324,1323],[2,8,25,64,6250]]
    found={};rng=random.Random(31)
    while len(found)<4:
        k=rng.choice([5,6,7]);H,M=(sparse_make(k,rng) if rng.random()<.5 else make2(k,rng,*rng.choice([([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3)])))
        if sorted(M) in targets and tuple(sorted(M)) not in found:found[tuple(sorted(M))]=H
    for M,H in found.items():
        S=diff_roots_rule(H);print('тайные',list(M),'ответ',len(M),'-> степени+корни:',len(S) if S else None,flush=True)

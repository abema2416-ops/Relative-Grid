from ens import *
def vexp(h,p):
    e=0
    while h%p==0:h//=p;e+=1
    return e
def sums(S):
    r={0}
    for x in S:r|={a+x for a in r}
    return r
def pieces_for(E,maxk=6):
    E=sorted(set(e for e in E if e>0))
    if not E:return []
    cand=sorted(set(E)|{abs(a-b) for a in E for b in E if a!=b}-{0})
    for k in range(1,maxk+1):
        for S in itertools.combinations_with_replacement(cand,k):
            if all(e in sums(S) for e in E):return sorted(S,reverse=True)
    return E
def split(e,S):
    # which pieces build exponent e: take from the largest (author: "накладываем самое большое")
    for k in range(len(S)+1):
        for c in itertools.combinations(range(len(S)),k):
            if sum(S[i] for i in c)==e:return c
    return None
def power_rule(H):
    """author's 'степенной метод': per prime, the exponents are sums of a few 'pieces' (2^8, 2^4, 2^3, 2^2 ...);
    find the fewest pieces, then merge pieces of different primes that are used by exactly the same heights"""
    P=[p for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43) if any(h%p==0 for h in H)]
    use={}
    for p in P:
        S=pieces_for([vexp(h,p) for h in H])
        for h in H:
            c=split(vexp(h,p),S)
            if c is None:return None
            for i in c:use.setdefault((p,i,S[i]),set()).add(h)
    groups={}
    for (p,i,e),hs in use.items():groups.setdefault(frozenset(hs),[]).append(p**e)
    M=[math.prod(v) for v in groups.values()]
    if not all(can_build(h,M) for h in H):
        for h in sorted(H):
            if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:d)
if __name__=="__main__":
    F=json.load(open('last3.json'))
    for f in F:
        S=power_rule(f['H']);print('тварина',f['M'],'ответ',f['k'],'степенной:',len(S),sorted(S))
    rng=random.Random(2027)
    while True:
        k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
        if sorted(M)==[4,8,45,81,625,6075,8100]:break
    S=power_rule(H);print('новая тварина ответ 7, степенной:',len(S),sorted(S))
    d=json.load(open('boss.json'));S=power_rule(d['H']);print('босс 9, степенной:',len(S))

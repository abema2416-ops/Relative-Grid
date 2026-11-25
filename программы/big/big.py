import random, itertools, math, sys, time
from collections import Counter
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
def fac(n):
    r={}
    for p in P:
        while n%p==0:r[p]=r.get(p,0)+1;n//=p
    assert n==1;return r
def divisors(n):
    f=fac(n);ds=[1]
    for p,e in f.items():ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def can_build(h,M):
    reach={1}
    for m in M:
        if h%m:continue
        reach|={r*m for r in reach if h%(r*m)==0}
        if h in reach:return True
    return h in reach
def ok(M,H):return all(can_build(h,M) for h in H)
def prune(M,H,key):
    M=list(M)
    for d in sorted(set(M),key=key):
        while d in M:
            T=list(M);T.remove(d)
            if all(can_build(h,T) for h in H if h%d==0):M=T
            else:break
    return M
# --- the author's rules ---
def rule_small_first(H):
    M=[]
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return len(M)
def rule_primes(H):
    mx={}
    for h in H:
        for p,e in fac(h).items():mx[p]=max(mx.get(p,0),e)
    return sum(mx.values())
def counts(H):
    C=Counter()
    for h in H:
        for d in divisors(h):
            if d>1:C[d]+=1
    return C
def rule_freq(H):
    C=counts(H);M=[];nb=0
    for d in sorted(C,key=lambda d:(-C[d],-d)):
        if C[d]<2:break
        while True:
            T=M+[d];b=sum(can_build(h,T) for h in H)
            if b>nb:M=T;nb=b
            else:break
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return len(prune(M,H,lambda d:(C[d],d)))
def rule_modes(H,key):
    C=counts(H);M=[d for d in C if C[d]>=2]
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return len(prune(M,H,lambda d:key(d,C)))
KEYS=[lambda d,C:(C[d],d),lambda d,C:(C[d],-d),lambda d,C:(-d,),lambda d,C:(d,)]
def rule_combo(H,big=True):
    G=sorted({math.gcd(a,b) for a,b in itertools.combinations(H,2)}-{1},reverse=True);M=list(G)
    for h in sorted(H):
        if can_build(h,M):continue
        g=max([g for g in G if h%g==0],default=1);q=h//g
        M.append(q if q>1 else h)
        if not can_build(h,M):M.append(h)
    return len(prune(M,H,(lambda d:d) if big else (lambda d:-d)))
def all_rules(H):
    lb=math.ceil(math.log2(len(H)+1));r={}
    for name,f in [('по порядку',rule_small_first),('простые',rule_primes),('комбинации',lambda H:min(rule_combo(H),rule_combo(H,False))),('частота',rule_freq),('моды',lambda H:min(rule_modes(H,k) for k in KEYS[:2]))]:
        r[name]=f(H)
        if min(r.values())==lb:break      # certificate: rules already equal the proven lower bound
    return min(r.values()),r
# --- planted hard instances with a certified answer ---
def make(k,rng):
    while True:
        M=[]
        while len(M)<k:
            m=1
            for _ in range(rng.randint(1,2)):m*=rng.choice(P)**rng.randint(1,2)
            if m>1 and m not in M:M.append(m)
        prods={}
        good=True
        for r in range(1,k+1):
            for c in itertools.combinations(M,r):
                v=math.prod(c)
                if v in prods:good=False;break
                prods[v]=c
            if not good:break
        if not good:continue
        allH=sorted(prods);s=rng.randint(2**(k-1),2**k-1)
        return sorted(rng.sample(allH,s)),M
seed=int(sys.argv[1]);N=int(sys.argv[2]);rng=random.Random(seed)
okc=0;t0=time.time()
for i in range(N):
    k=rng.choice([5,6,7]);H,M=make(k,rng)
    t=time.time();best,r=all_rules(H);dt=time.time()-t
    lb=math.ceil(math.log2(len(H)+1))
    okc+=best==k
    print(f"{i+1:3d}. высот {len(H):3d}, крупнейшая {max(H):.2e} ({len(str(max(H)))} цифр), ответ {k} (доказан: нижняя {lb} = спрятанный набор {k}); правила {best} {'✓' if best==k else '✗'} [{dt:.1f} c] {r}",flush=True)
print('ИТОГО',okc,'из',N,'за',round(time.time()-t0),'c',flush=True)

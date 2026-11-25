import itertools, random, math
from fractions import Fraction
def cands(H):
    H=sorted(set(H)); D=set()
    for a,b in itertools.combinations(H,2):
        g=math.gcd(a,b)
        for d in range(2,g+1):
            if g%d==0: D.add(d)
    Q={h//d for h in H for d in D if h%d==0 and h//d>=2}
    return sorted(set(H)|D|Q)
def ok(M,H):
    prods=set()
    for r in range(1,len(M)+1):
        for S in itertools.combinations(M,r):
            prods.add(math.prod(S))
    return all(h in prods for h in H)
def R(H):
    C=cands(H)
    for k in range(1,len(H)+1):
        for M in itertools.combinations_with_replacement(C,k):
            if ok(M,H): return k
# power chains
for b in [2,3,6]:
    for D in range(1,8):
        H=[b**e for e in range(1,D+1)]
        r=R(H); assert r==math.ceil(math.log2(D+1)),(b,D,r)
print("power chains ok")
# pairwise coprime
pr=[2,3,5,7,11,13,4*1,9,25,49]
for _ in range(300):
    ps=random.sample([2,3,5,7,11,13],random.randint(1,5))
    H=set()
    for p in ps: H.add(p**random.randint(1,3))
    H=sorted(H)
    assert R(H)==len(H),H
print("coprime ok")
# bounds
for _ in range(400):
    H=sorted(set(random.randint(2,60) for _ in range(random.randint(1,6))))
    r=R(H); assert math.ceil(math.log2(len(H)+1))<=r<=len(H)
print("bounds ok")
# exact alpha stretch: figure of alpha(O) == T(figure of G) ∪ rest, n=1 check with intervals
for _ in range(2000):
    O=set(random.sample(range(-10,10),random.randint(1,8)));G=set(c for c in O if random.random()<.6)
    if not G: continue
    s=random.choice([1,-1]); f=random.randint(2,4)
    a=min(s*c for c in G)
    new={s*(a+f*(s*c-a)+j) for c in G for j in range(f)}
    # continuous: cell c occupies s-interval [s*c, s*c+1) (for s=-1 use mirrored coords); T(y)=a+f(y-a)
    cont=set()
    for c in G:
        lo=a+f*(s*c-a); hi=a+f*(s*c+1-a)
        cont|={s*p for p in range(lo,hi)}
    assert new==cont
print("stretch exact ok")

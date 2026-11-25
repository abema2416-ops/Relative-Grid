exec(open('mode.py').read().split("H=[4,6,7,8,21,24]")[0])
import time
def combo_rule(H,keep_big=True):
    # author: repeated combinations of prime factors (common sub-products of two heights = gcd) are one component
    H=[h for h in set(H) if h>1]
    G=set()
    for a,b in itertools.combinations(H,2):
        g=math.gcd(a,b)
        if g>1:G.add(g)
    M=sorted(G,reverse=True)
    # leftovers: what each height still needs after its biggest usable component
    for h in sorted(H):
        if h in gen(M):continue
        best=None
        for g in M:
            if h%g==0 and (best is None or g>best):best=g
        q=h//best if best else h
        if q>1 and h not in gen(M+[q]):M.append(h)
        elif q>1:M.append(q)
    for h in sorted(H):
        if h not in gen(M):M.append(h)
    order=sorted(M,key=(lambda d:d) if keep_big else (lambda d:-d))   # try to drop small first (keep big combos)
    for d in order:
        T=list(M);T.remove(d)
        if all(h in gen(T) for h in H):M=T
    return len(M)
def everything(H):return min(min(mode_rule(H,f) for f in keys.values()),allbest(H),freq_rule(H))
H=[2,10,22,24,41,60];print('пример',rmin(H),combo_rule(H),combo_rule(H,False),everything(H))
random.seed(11);t=time.time();n=ok=okc=0
while time.time()-t<1200:
    H=set(random.sample(range(2,61),random.randint(3,7)))
    a=rmin(H);c=min(combo_rule(H),combo_rule(H,False));b=min(everything(H),c);n+=1;ok+=a==b;okc+=a==c
    if c<a:print('UNDER',H)
    if a!=b:print('BAD',sorted(H),b,a,flush=True)
print('tested',n,'all rules exact',ok,'combo alone',okc,flush=True)

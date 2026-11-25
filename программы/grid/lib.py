import itertools, math, random
def gen(M):
    s={1}
    for f in M: s|={x*f for x in s}
    return s
def rmin(H):
    H=[h for h in set(H) if h>1]
    if not H:return 0
    cands=sorted({d for h in H for d in range(2,h+1) if h%d==0})
    for k in range(1,9):
        for M in itertools.combinations_with_replacement(cands,k):
            if all(h in gen(M) for h in H):return k
def rule3(H):
    M=[]
    for h in sorted(set(x for x in H if x>1)):
        if h not in gen(M):M.append(h)
    return len(M)

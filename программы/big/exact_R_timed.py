import itertools as it, math, time, random, sys, json
def cands(H):
    H=sorted(set(h for h in H if h>1)); C=set(H); D=set()
    for a,b in it.combinations(H,2):
        g=math.gcd(a,b)
        if g>1:
            for d in range(2,int(g**0.5)+1):
                if g%d==0: D.add(d); D.add(g//d)
            D.add(g)
    C|=D; C|={h//d for h in H for d in D if h%d==0 and h//d>=2}
    return sorted(C)
def R_le(H,k,C,deadline):
    H=sorted(set(h for h in H if h>1))
    for M in it.combinations_with_replacement(C,k):
        if time.time()>deadline: return None
        pr=set()
        for r in range(1,k+1):
            for S in it.combinations(M,r): pr.add(math.prod(S))
        if all(h in pr for h in H): return M
    return False
H=json.load(open(sys.argv[1]))[0]['H']; C=cands(H)
print('кандидатов',len(C),flush=True)
t=time.time(); r=R_le(H,6,C,t+float(sys.argv[2])); print('R<=6:',r,'за',round(time.time()-t,1),'с')

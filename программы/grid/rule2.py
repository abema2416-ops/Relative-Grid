exec(open('rmin.py').read().split('tests=')[0])
import random, itertools
def products(others):  # products of sub-multisets of size>=2 of others (each height used once)
    s=set();o=list(others)
    for k in range(2,len(o)+1):
        for c in itertools.combinations(o,k):s.add(math.prod(c))
    return s
def rule2(H):
    H=set(h for h in H if h>1);c=0
    for h in H:
        if isprime(h):c+=1
        else:c+= 0 if h in products(H-{h}) else 1
    return c
tests=[{2,3,6},{2,4},{2,3,4},{2,3,12},{2,3,6,9},{6,10,15,30},{2,3,6,12},{2,3,5,30},{4,8},{2,4,8},{6}]
for H in tests:print(sorted(H),rmin(H),rule2(H))
random.seed(1);bad=0;N=400;ex=[]
for _ in range(N):
    H=set(random.sample(range(2,31),random.randint(2,5)))
    a,b=rmin(H),rule2(H)
    if a!=b:bad+=1;ex.append((sorted(H),a,b))
print('mismatch',bad,'of',N);print(ex[:8])
print('rule2 < rmin cases:',sum(1 for e in ex if e[2]<e[1]))

from lib import *
import sys,time
src=open('rule8.py').read();i=src.index('def common_divs');exec(src[i:src.index('def greedy',i)])
def rmin_fast(H,cap=7):
    H=[h for h in set(H) if h>1]
    cands=sorted({d for h in H for d in range(2,h+1) if h%d==0})
    for k in range(1,cap+1):
        for M in itertools.combinations_with_replacement(cands,k):
            if all(h in gen(M) for h in H):return k
    return None
random.seed(int(sys.argv[1]));found=[];tested=0;t0=time.time()
while time.time()-t0<float(sys.argv[2]):
    # structured: heights built as products of a hidden multiplier set
    M=[random.choice([2,2,3,3,5,7,11,13,4,6,9]) for _ in range(random.randint(3,5))]
    H=set()
    for _ in range(random.randint(3,6)):
        sub=[m for m in M if random.random()<.5]
        if sub:H.add(math.prod(sub))
    H={h for h in H if 1<h<=400}
    if len(H)<3:continue
    a=rmin_fast(H);b=rmin_restricted(H);tested+=1
    if a!=b:found.append((sorted(H),a,b));print('COUNTEREXAMPLE',sorted(H),a,b,flush=True)
    if len(found)>=3:break
print('tested',tested,'counterexamples',len(found))

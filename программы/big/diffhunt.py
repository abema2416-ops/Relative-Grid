from diff import *
import sys
rng=random.Random(int(sys.argv[1]));t=time.time();n=ok=okd=0
while time.time()-t<float(sys.argv[2]):
    k=rng.choice([5,6,7]);H,M=(sparse_make(k,rng) if rng.random()<.5 else make2(k,rng,*rng.choice([([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3)])))
    S=diff_rule(H);d=len(S) if S else 99;n+=1;okd+=d==k
    if d!=k:
        b,_=ensemble(H);d=min(d,b)
    ok+=d==k
    if d!=k:print('ТВАРИНА',sorted(M),len(H),k,d,flush=True)
print('задач',n,'| разность степеней одна:',okd,'| вместе со всеми:',ok,flush=True)

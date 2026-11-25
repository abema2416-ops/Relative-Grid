from structrule import *
from pipe import sparse_make, method_v1
rng=random.Random(99);out=[]
for i in range(277):
    k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
    s=len(rule_struct(H))
    if s!=k:
        b,_=method_v1(H)
        if min(s,b)!=k:out.append({'H':H,'M':sorted(M),'k':k,'struct':s,'old':b});print(len(H),sorted(M),k,s,b,flush=True)
json.dump(out,open('last3.json','w'))

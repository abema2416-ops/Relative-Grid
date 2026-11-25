from structrule import *
from pipe import sparse_make, method_v1
F=json.load(open('fails_21.json'))+json.load(open('fails_22.json'))
print('прежние 10 тварин: решено',sum(len(rule_struct(f['H']))==f['k'] for f in F),'из',len(F),flush=True)
rng=random.Random(99);t=time.time();n=ok_s=ok_all=0
while time.time()-t<420:
    k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
    s=len(rule_struct(H));n+=1;ok_s+=s==k
    if s!=k:
        b,_=method_v1(H);s=min(s,b)
    ok_all+=s==k
print('новые «редкие» задачи:',n,'| новое правило одно:',ok_s,'| вместе со старыми:',ok_all,flush=True)

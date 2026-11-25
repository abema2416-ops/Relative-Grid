import sys
from bigmode import *
rng=random.Random(int(sys.argv[1]));t0=time.time();n=0;bad=0
configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
while time.time()-t0<float(sys.argv[2]):
    pool,maxe,maxp=rng.choice(configs);k=rng.choice([5,6])
    H,M=make2(k,rng,pool,maxe,maxp);lb=math.ceil(math.log2(len(H)+1))
    best,r=all_rules2(H)
    if best!=k:
        for nme,s in SC.items():
            r['бол. мода: '+nme]=len(improve(H,rule_bigmode(H,s)))
            if min(r.values())==k:break
    best=min(r.values());n+=1
    if best!=k:bad+=1;print('CE',k,best,sorted(M),len(H),flush=True)
print('tested',n,'bad',bad,flush=True)

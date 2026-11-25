import sys
from gold import greedy_gold, make2, all_rules2, improve, rule_bigmode, SC, math, random, time
G=lambda c,d:c*math.log(d)
rng=random.Random(int(sys.argv[1]));t0=time.time();n=bad=0;gold_needed=0
configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
while time.time()-t0<float(sys.argv[2]):
    pool,maxe,maxp=rng.choice(configs);k=rng.choice([5,6]);H,M=make2(k,rng,pool,maxe,maxp)
    best,r=all_rules2(H)
    if best!=k:
        for nme,s in SC.items():
            r['бол. мода']=min(r.get('бол. мода',99),len(improve(H,rule_bigmode(H,s))))
        if min(r.values())!=k:
            r['золотая середина']=len(greedy_gold(H,G))
            if r['золотая середина']==k:gold_needed+=1
    n+=1
    if min(r.values())!=k:bad+=1;print('CE',k,min(r.values()),sorted(M),len(H),flush=True)
print('tested',n,'bad',bad,'gold rescued',gold_needed,flush=True)

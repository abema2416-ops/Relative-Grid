import sys, json
from gold import *
from dswap import improve2
GOLD=lambda c,d:c*math.log(d)
def method_v1(H):
    """all rules of the author so far (best of): order, primes, combos+swap, freq, modes, big mode, golden middle"""
    best,r=all_rules2(H);lb=math.ceil(math.log2(len(H)+1))
    if best==lb:return best,'v1'
    for nme,s in SC.items():
        best=min(best,len(improve(H,rule_bigmode(H,s))))
    best=min(best,len(greedy_gold(H,GOLD)))
    return best,'v1'
def gold_set(H):return greedy_gold(H,GOLD)
def method_v2(H,restarts=6,seed=0):
    """v1 + double swap + restarts with shuffled candidate orders"""
    b,_=method_v1(H);lb=math.ceil(math.log2(len(H)+1))
    if b==lb:return b
    S=improve2(H,gold_set(H));b=min(b,len(S))
    rr=random.Random(seed);C=counts(H)
    for t in range(restarts):
        if b==lb:break
        noise={d:rr.random()*0.6+0.7 for d in C}
        S=greedy_gold(H,lambda c,d:c*math.log(d)*noise[d]);S=improve2(H,S);b=min(b,len(S))
    return b
def sparse_make(k,rng):
    configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
    pool,maxe,maxp=rng.choice(configs)
    while True:
        H,M=make2(k,rng,pool,maxe,maxp)
        if len(H)<=2**(k-1)+3:return H,M     # the hardest kind: only about half of the products kept
if __name__=="__main__":
    seed=int(sys.argv[1]);T=float(sys.argv[2]);rng=random.Random(seed);t0=time.time();out=[];n=0
    while time.time()-t0<T:
        k=rng.choice([5,6]);H,M=sparse_make(k,rng);b,_=method_v1(H);n+=1
        if b!=k:out.append({'H':H,'M':sorted(M),'k':k,'v1':b});print('CE',k,b,sorted(M),flush=True)
    json.dump(out,open(f'fails_{seed}.json','w'));print('tested',n,'fails',len(out),flush=True)

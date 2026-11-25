import sys
src=open('big2.py').read().split("seed=int(sys.argv[1])")[0];exec(src)
def make2(k,rng,pool,maxe,maxp):
    while True:
        M=[]
        while len(M)<k:
            m=1
            for _ in range(rng.randint(1,maxp)):m*=rng.choice(pool)**rng.randint(1,maxe)
            if m>1 and m not in M:M.append(m)
        prods={};good=True
        for r in range(1,k+1):
            for c in itertools.combinations(M,r):
                v=math.prod(c)
                if v in prods:good=False;break
                prods[v]=c
            if not good:break
        if not good:continue
        allH=sorted(prods);s=rng.randint(2**(k-1),2**k-1)
        return sorted(rng.sample(allH,s)),M
rng=random.Random(int(sys.argv[1]));t0=time.time();n=0
configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
while time.time()-t0<float(sys.argv[2]):
    pool,maxe,maxp=rng.choice(configs);k=rng.choice([5,6])
    H,M=make2(k,rng,pool,maxe,maxp);best,r=all_rules2(H);n+=1
    if best!=k:print('CE',k,best,sorted(M),H,r,flush=True);break
print('tested',n,flush=True)

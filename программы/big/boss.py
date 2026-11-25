from gold import *
rng=random.Random(2026)
def gen(k,pool,maxe,maxp,keep):
    while True:
        M=[]
        while len(M)<k:
            m=1
            for _ in range(rng.randint(2,maxp)):m*=rng.choice(pool)**rng.randint(1,maxe)
            if m>1 and m not in M:M.append(m)
        prods={};good=True
        for r in range(1,k+1):
            for c in itertools.combinations(M,r):
                v=math.prod(c)
                if v in prods:good=False;break
                prods[v]=c
            if not good:break
        if good:
            H=sorted(rng.sample(sorted(prods),keep));return H,sorted(M)
k=9;H,M=gen(k,[2,3,5,7],3,3,2**(k-1)+1)
print('высот',len(H),'цифр в самой большой',len(str(max(H))),'граница',math.ceil(math.log2(len(H)+1)))
import json;json.dump({'H':H,'M':M},open('boss.json','w'))
t=time.time()
for name,f in [('по порядку',rule_small_first),('простые',rule_primes),('комбинации',lambda H:min(rule_combo(H),rule_combo(H,False)))]:
    print(name,f(H),round(time.time()-t),flush=True)
print('золотая середина',len(greedy_gold(H,lambda c,d:c*math.log(d))),round(time.time()-t),flush=True)

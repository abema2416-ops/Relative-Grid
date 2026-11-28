import math, random, subprocess, sys
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
rng=random.Random(77)
for i in range(30):
    kind=i%3
    if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng)
    elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3)
    else:
        P=[2,3,5,7,11,13,17,19,23,29,31,37]; u=rng.choice([10,12]); Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        H=sorted(Hs)
        if i+1 in (9,15,24):
            masks=[sum(1<<j for j,p in enumerate(P[:u]) if h%p==0) for h in H]
            g=sum(1 for a in range(len(H)) for b in range(a+1,len(H)) if math.gcd(H[a],H[b])>1)
            lb=rank(H); print(f"задача {i+1}: высот {len(H)}, простых {u}, пар с общим делителем {g}, ранг {lb}",flush=True)
            out=subprocess.run(['./core_exact',sys.argv[1],str(lb),str(len(H))],input=f"{len(H)} {u}\n"+" ".join(map(str,masks)),capture_output=True,text=True).stdout
            print(out,flush=True)

import math, random, subprocess, sys
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
rng=random.Random(77); inst={}
for i in range(30):
    kind=i%3
    if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng)
    elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3)
    else:
        P=[2,3,5,7,11,13,17,19,23,29,31,37]; u=rng.choice([10,12]); Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        inst[i+1]=(sorted(Hs),u)
P=[2,3,5,7,11,13,17,19,23,29,31,37]
# проверка найденных ответов 15 и 24
for j,bl in [(15,[128,1029,600,521,3139,2305,48,8,1062,3858,1104]),(24,[96,776,256,596,18,144,1,4,40])]:
    H,u=inst[j]; M=[math.prod(p for t,p in enumerate(P[:u]) if b>>t&1) for b in bl]
    S={1}
    for m in M: S|={x*m for x in S}
    print(f"задача {j}: множители {sorted(M)} — собирают все высоты: {all(h in S for h in H)}",flush=True)
H,u=inst[9]; masks=[sum(1<<t for t,p in enumerate(P[:u]) if h%p==0) for h in H]
print("задача 9: высоты",H,flush=True)
p=subprocess.run(['./core_exact',sys.argv[1],'11','12'],input=f"{len(H)} {u}\n"+" ".join(map(str,masks)),capture_output=True,text=True)
print(p.stdout, p.stderr[-300:],flush=True)

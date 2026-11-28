import math, random, time, sys, subprocess, os
sys.path.insert(0,'/tmp/hell'); sys.path.append('/home/claude/relative-grid/программы/big')
exec(open('/tmp/hell/gcd_kent2.py').read().split("d=json.load")[0])
os.chdir('/home/claude/relative-grid/программы/big')
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
subprocess.run(['g++','-O2','-o','/tmp/hell/core_exact','core_exact.cpp'])
PR=[p for p in range(2,200) if all(p%q for q in range(2,int(p**0.5)+1))]
def team(H,limit):
    t=time.time(); fs=[fac(h) for h in H]; ps=sorted({p for f in fs for p in f})
    pat={}
    for p in ps: pat.setdefault(tuple(p in f for f in fs),[]).append(p)
    lb=max(rank(H),math.ceil(math.log2(len(H)+1))); ub=min(len(H),len(pat)); who='счёт'
    Mg,ok=gcd_kent2(H,lambda u,k:(u-1)*(k-1))
    if ok and len(Mg)<ub: ub=len(Mg); who='НОД'
    if lb==ub: return lb,lb,ub,who,time.time()-t
    groups=list(pat.values()); gi={p:i for i,g in enumerate(groups) for p in g}
    masks=[sum(1<<gi[p] for p in f) for f in fs]
    if len(groups)>31: return None,lb,ub,'слишком много полос для решателя',time.time()-t
    out=subprocess.run(['/tmp/hell/core_exact',str(limit),str(lb),str(ub-1)],input=f"{len(H)} {len(groups)}\n"+" ".join(map(str,masks)),capture_output=True,text=True).stdout
    if 'R =' in out: k=int(out.split('R =')[1].split()[0]); return k,lb,k,'решатель',time.time()-t
    if 'не успел' not in out: return ub,lb,ub,who+', доказано',time.time()-t
    return None,lb,ub,'ВИЛКА: никто не взял',time.time()-t
rng=random.Random(4242)
for u in []:
    for i in range(3):
        Hs=set()
        while len(Hs)<u:
            S=[p for p in PR[:u] if rng.random()<0.35]
            if S: Hs.add(math.prod(S))
        r=team(sorted(Hs),60)
        print(f"простых {u}, высот {u}: ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)

print("--- задачи с перекрывающимися тайными кусками ---",flush=True)
def planted(seed,u,k,D):
    r=random.Random(seed); P=PR[:u]
    while True:
        B=[frozenset(r.sample(P,r.randint(3,5))) for _ in range(k)]
        if len(set(B))<k: continue
        Hs=set(); tries=0
        while len(Hs)<D and tries<20000:
            tries+=1; c=r.sample(range(k),r.choice([2,2,3]))
            if len(frozenset().union(*[B[i] for i in c]))==sum(len(B[i]) for i in c): Hs.add(math.prod(frozenset().union(*[B[i] for i in c])))
        if len(Hs)==D: return sorted(Hs)
for (u,k,D) in [(16,12,20),(20,14,24),(24,18,30),(28,20,36)]:
    for s in range(3):
        r=team(planted(100*u+s,u,k,D),60)
        print(f"простых {u}, тайно ≤{k}, высот {D}: ответ {r[0]}, низ {r[1]}, верх {r[2]} — {r[3]} ({r[4]:.1f} с)",flush=True)

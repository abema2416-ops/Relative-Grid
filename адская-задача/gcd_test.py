import math, random, time, sys, json
sys.path.insert(0,'/tmp/hell'); sys.path.append('/home/claude/relative-grid/программы/big')
exec(open('/tmp/hell/gcd_kent2.py').read().split("d=json.load")[0])
P=[2,3,5,7,11,13,17,19,23,29,31,37]
import os; os.chdir('/home/claude/relative-grid/программы/big')
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
sc=lambda u,k:(u-1)*(k-1)
rng=random.Random(77); known={3:12,6:10,9:12,12:10,15:11,18:12,21:10,24:9,27:10,30:10}
for i in range(30):
    kind=i%3
    if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng)
    elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3)
    else:
        u=rng.choice([10,12]); Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        H=sorted(Hs); Mg,ok=gcd_kent2(H,sc)
        print(f"задача {i+1:2d}: кент НОД {len(Mg)} (собирает: {ok}), точный ответ {known[i+1]} {'ТОЧНО' if len(Mg)==known[i+1] else ''}")
for name,H,ans in [("8 высот",[130,143,357,2210,6783,8645,440895,881790],7),("9 высот",[11,357,1463,2618,3705,4485,7293,8211,34034],8)]:
    Mg,ok=gcd_kent2(H,sc); print(f"{name}: кент НОД {len(Mg)} (собирает: {ok}), точный ответ {ans} {'ТОЧНО' if len(Mg)==ans else ''}")
# ещё 5 адских задач с другими тайнами
sys.path.insert(0,'/tmp/hell')
exec(open('/tmp/hell/make_hell.py').read().split("H,M,used=make(666)")[0])
for seed in [1,2,3,4,5]:
    H,M,used=make(seed); t=time.time(); Mg,ok=gcd_kent2(H,sc); rk=rank(H)
    print(f"адская #{seed}: высот {len(H)}, тайно {len(M)}, ранг {rk}, кент НОД {len(Mg)} (собирает: {ok}) за {time.time()-t:.1f} с {'ТОЧНО (= ранг)' if len(Mg)==rk else ''}",flush=True)

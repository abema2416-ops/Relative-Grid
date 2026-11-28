import sys, json, math, random
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
exec(open('rank_bound.py').read().split("def rank")[0].split("exec(open")[0]) if False else None
import re
ans={}
for f in ['giga30.txt','giga_fast.txt']:
    for l in open(f):
        m=re.match(r'\s*(\d+)\. .* ответ (\d+)',l)
        if m: ans[int(m.group(1))]=int(m.group(2))
rng=random.Random(77); rows=[]
for i in range(30):
    kind=i%3
    if kind==0: k=rng.choice([6,7]); H,M=sparse_make(k,rng); name=f'спрятано {k}'
    elif kind==1: k=rng.choice([7,8,9]); H,M=make2(k,rng,[2,3,5,7,11,13],2,3); name=f'спрятано {k}'
    else:
        P=[2,3,5,7,11,13,17,19,23,29,31,37]; u=rng.choice([10,12]); Hs=set()
        while len(Hs)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: Hs.add(math.prod(S))
        H=sorted(Hs); name=f'перемешано {u}'
    lg=math.ceil(math.log2(len(set(H))+1)); rk=rank(H); a=ans.get(i+1)
    rows.append((i+1,name,len(H),lg,rk,a))
    print(f"{i+1:2d}. {name:14s} высот {len(H):3d}  log {lg:2d}  ранг {rk:2d}  ответ {a}",flush=True)
c_log=sum(1 for r in rows if r[5] and r[3]==r[5]); c_rk=sum(1 for r in rows if r[5] and r[4]==r[5]); c_any=sum(1 for r in rows if r[5] and max(r[3],r[4])==r[5]); known=sum(1 for r in rows if r[5])
print(f"ответ известен: {known}; граница точна — log: {c_log}, ранг: {c_rk}, лучшая из двух: {c_any}")

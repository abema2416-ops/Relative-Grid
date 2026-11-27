import sys, random, math, time, json
from fractions import Fraction
exec(open('superkent.py').read().split("H=json.load")[0])
def fac(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def rank(H):
    F=[fac(h) for h in H]; P=sorted({p for f in F for p in f})
    A=[[Fraction(f.get(p,0)) for p in P] for f in F]; r=0; cols=len(P)
    for c in range(cols):
        piv=next((i for i in range(r,len(A)) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]!=0:
                k=A[i][c]/A[r][c]; A[i]=[x-k*y for x,y in zip(A[i],A[r])]
        r+=1
    return r
# 1) старый контрпример
H=json.load(open('fails_7.json'))[0]['H']
print("контрпример: R=6, log-граница", math.ceil(math.log2(len(H)+1)), "ранговая граница", rank(H))
# 2) трудные «перемешанные» задачи
P=[2,3,5,7,11,13,17,19,23,29,31,37]
rng=random.Random(9); viol=0
for u in [6,8,10]:
    for i in range(6):
        H=set()
        while len(H)<u:
            S=[p for p in P[:u] if rng.random()<0.4]
            if S: H.add(math.prod(S))
        H=sorted(H); rk=rank(H); lb=math.ceil(math.log2(len(H)+1))
        t=time.time()
        try: R,_,_=solve(H,len(H),t+30); 
        except TimeoutError: R=None
        if R is not None and R<rk: viol+=1
        print(f"простых {u}: R = {R}, ранг = {rk}, log-граница = {lb}, {'ранг = ответ, СЕРТИФИКАТ' if R==rk else ''}",flush=True)
print("нарушений R ≥ ранг:",viol)

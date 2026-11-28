"""МЕТОД ЗАФАРОВА — порядок действий, который по набору высот H выдаёт формулу ответа и проверяет её.
Шаг 1 разложить; 2 узнать узор; 3 нижняя граница; 4 кенты по очереди; 5 точный поиск; 6 деревья; 7 формула+проверка."""
import math, time, sys, json, subprocess, os, itertools
from fractions import Fraction
from collections import Counter
BIG='/home/claude/relative-grid/программы/big'
def fac(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1 if p==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f
def rank(F,ps):
    A=[[Fraction(f.get(p,0)) for p in ps] for f in F]; r=0
    for c in range(len(ps)):
        pv=next((i for i in range(r,len(A)) if A[i][c]!=0),None)
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]!=0:
                k=A[i][c]/A[r][c]; A[i]=[x-k*y for x,y in zip(A[i],A[r])]
        r+=1
    return r
def decompose(h,M):                     # формула высоты: h = произведение части M (без 2^k)
    ds=sorted([m for m in M if h%m==0],reverse=True)
    def go(r,i,acc):
        if r==1: return acc
        for j in range(i,len(ds)):
            if r%ds[j]==0:
                res=go(r//ds[j],j+1,acc+[ds[j]])
                if res is not None: return res
        return None
    return go(h,0,[])
def check(H,M): return all(decompose(h,M) is not None for h in H)
def jumps_kent(H,lb):
    C=Counter(b//a for a in H for b in H if b>a and b%a==0)
    for h in H: C[h]+=1
    top=[d for d,_ in C.most_common(lb+3)]
    for k in range(lb,min(len(top),lb+3)+1):
        for M in itertools.combinations(top,k):
            if check(H,M): return list(M)
    return None
def gcd_kent(H):
    sq=lambda g,r: r%g==0 and math.gcd(g,r//g)==1
    rest={h:h for h in H}; ch=[]
    while True:
        todo=[r for r in rest.values() if r>1]
        if not todo: break
        C=Counter(math.gcd(a,b) for a,b in itertools.combinations(todo,2))
        best=None
        for g in C:
            if g<2: continue
            u=sum(1 for r in todo if sq(g,r))
            if u<2: continue
            s=(u-1)*(len(fac(g))-1)
            if best is None or s>best[0]: best=(s,g)
        if not best: ch+=list(set(todo)); break
        g=best[1]; ch.append(g)
        for h in rest:
            if sq(g,rest[h]): rest[h]//=g
    ch=sorted(set(ch)); return ch if check(H,ch) else None
def metod(H,limit=60,log=print):
    T0=time.time(); H=sorted(set(h for h in H if h>1)); D=len(H)
    # 1. разложить
    F=[fac(h) for h in H]; ps=sorted({p for f in F for p in f}); sqf=all(max(f.values())==1 for f in F)
    pat={}
    for p in ps: pat.setdefault(tuple(f.get(p,0) for f in F),[]).append(p)
    log(f"1. высот {D}, простых {len(ps)}, разных полос {len(pat)}, без квадратов: {sqf}")
    # 2. узнать узор
    if all(math.gcd(a,b)==1 for a,b in itertools.combinations(H,2)):
        return finish(H,H,D,D,"узор: высоты попарно взаимно простые ⇒ R = D",T0,log)
    if len(ps)==1:
        p=ps[0]; E=sorted(f[p] for f in F)
        if E==list(range(1,len(E)+1)):
            k=math.ceil(math.log2(D+1)); M=[p**(2**i) for i in range(k)]
            return finish(H,M,k,k,"узор: лесенка степеней ⇒ R = ⌈log₂(D+1)⌉",T0,log)
    # 3. нижняя граница
    rk=rank(F,ps); lb=max(rk,math.ceil(math.log2(D+1))); log(f"3. нижняя граница: ранг {rk}, логарифм {math.ceil(math.log2(D+1))} ⇒ L = {lb}")
    # 4. кенты по очереди
    best=list(H); who='счёт высот'
    if sqf:
        Mst=[math.prod(g) for g in pat.values()]
        if len(Mst)<len(best) and check(H,Mst): best=Mst; who='полосы'
    for name,fn in [('скачки',lambda: jumps_kent(H,lb)),('НОД',lambda: gcd_kent(H))]:
        t=time.time(); M=fn()
        log(f"4. кент «{name}»: {len(M) if M else '—'} ({time.time()-t:.1f} с)")
        if M and len(M)<len(best): best=M; who=name
        if len(best)==lb: return finish(H,best,lb,lb,f"кент «{who}» = нижней границе",T0,log)
    ub=len(best); log(f"   верхняя граница U = {ub} (кент «{who}»)")
    # 5. точный поиск (решатель на масках для бесквадратных; иначе суперкент)
    left=max(1,int(limit-(time.time()-T0)))
    if sqf and len(pat)<=31:
        groups=list(pat.values()); gi={p:i for i,g in enumerate(groups) for p in g}
        masks=[sum(1<<gi[p] for p in f) for f in F]
        out=subprocess.run(['./core_exact',str(left),str(lb),str(ub-1)],input=f"{D} {len(groups)}\n"+" ".join(map(str,masks)),capture_output=True,text=True).stdout
        if 'R =' in out:
            k=int(out.split('R =')[1].split()[0]); bl=[int(x) for x in out.split('блоки:')[1].split()]
            M=[math.prod(math.prod(groups[i]) for i in range(len(groups)) if b>>i&1) for b in bl]
            return finish(H,M,k,k,"точный поиск (маски) от нижней границы",T0,log)
        if 'не успел' not in out: return finish(H,best,ub,ub,f"точный поиск доказал: меньше {ub} нельзя",T0,log)
        log(f"5. точный поиск не успел за {left} с")
    # 6. итог: вилка
    return finish(H,best,lb,ub,"вилка (лучшее найденное)",T0,log)
def finish(H,M,lb,ub,why,T0,log):
    ok=check(H,M)
    log(f"7. ОТВЕТ: {'R = '+str(len(M)) if lb==ub else f'{lb} ≤ R ≤ {ub}'} — {why}; проверка: {'все высоты собраны' if ok else 'ОШИБКА'}; {time.time()-T0:.1f} с")
    return {'lb':lb,'ub':ub,'M':sorted(M),'why':why,'ok':ok,'formula':{h:decompose(h,M) for h in H}}
if __name__=="__main__":
    subprocess.run(['g++','-O2','-o','./core_exact',BIG+'/core_exact.cpp'])
    tests=[("лесенка",[3**e for e in range(1,9)]),("взаимно простые",[4,9,25,49,11]),
           ("гигабосс",json.load(open(BIG+'/boss.json'))['H']),
           ("адская (150 высот)",json.load(open('/home/claude/relative-grid/адская-задача/hell.json'))['H']),
           ("задача 9",[110,299,1218,4030,4070,17670,48433,787930,6697405,10068366,10818885,49560797]),
           ("босс-2",json.load(open('/home/claude/relative-grid/адская-задача/boss2.json'))['H'])]
    for name,H in tests:
        print(f"\n===== {name} =====",flush=True); r=metod(H,60)
        ex=list(r['formula'].items())[:2]
        print("   формула (пример):", "; ".join(f"{h} = {' · '.join(map(str,d))}" for h,d in ex),flush=True)

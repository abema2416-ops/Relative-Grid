import time, random, itertools, math, sys
S='/tmp/claude-0/-home-claude/70a5592c-c34c-5075-ac31-210cdddf20fb/scratchpad'
# ---------- (Г) полуобороты: наш счёт пересечений против интеграла Гаусса ----------
src=open(S+'/twist/tw.py').read().split("total=0;bad=0;hist={}")[0]
G={}; exec(src,G)
def gauss_lk(core,bnd,K):
    # классика: двойной интеграл Гаусса, численно (K точек на отрезок)
    def pts(segs):
        out=[]
        for (A,B) in segs:
            A=[float(x) for x in A];B=[float(x) for x in B]
            d=[(B[i]-A[i])/K for i in range(3)]
            for k in range(K): out.append(([A[i]+(k+.5)*d[i] for i in range(3)],d))
        return out
    P=pts(core);Q=pts(bnd);tot=0.0
    for p,dp in P:
        for q,dq in Q:
            r=[p[i]-q[i] for i in range(3)]; n=math.sqrt(sum(x*x for x in r))**3
            c=(dp[1]*dq[2]-dp[2]*dq[1],dp[2]*dq[0]-dp[0]*dq[2],dp[0]*dq[1]-dp[1]*dq[0])
            tot+=sum(r[i]*c[i] for i in range(3))/n
    return tot/(4*math.pi)
strips=G['find'](10,60)
pick=[c for c,o in strips]
t=time.time(); ours=[G['lk'](c)[0] for c in pick]; t_ours=time.time()-t
# для классики нужны те же кривые: достаём их из half_twists
def curves(cyc):
    import types
    V={s:G['sq_verts'](*s) for s in cyc}; n=len(cyc)
    from fractions import Fraction as Fr
    cen=lambda s: tuple(Fr(sum(p[i] for p in V[s]),4) for i in range(3))
    core=[];glued=set()
    for i in range(n):
        a,b=cyc[i],cyc[(i+1)%n];E=(set(G['edges'](V[a]))&set(G['edges'](V[b]))).pop();glued.add(E)
        p,q=tuple(E);core.append(cen(a));core.append(tuple(Fr(p[k]+q[k],2) for k in range(3)))
    cs=[(core[i],core[(i+1)%len(core)]) for i in range(len(core))]
    # край — как в tw.py (ориентированный)
    owner={}
    for i,sq in enumerate(cyc):
        for E in G['edges'](V[sq]):
            if E not in glued: owner[E]=i
    adjv={}
    for E in owner:
        for v in E: adjv.setdefault(v,[]).append(E)
    left=set(owner);bnd=[]
    while left:
        E0=left.pop();a,b=tuple(E0);loop=[(a,b,owner[E0])];cur=b
        while True:
            nx=[E for E in adjv[cur] if E in left]
            if not nx: break
            E=nx[0];left.discard(E);x,y=tuple(E);y=y if x==cur else x;loop.append((cur,y,owner[E]));cur=y
        w=0
        for k in range(len(loop)):
            d=(loop[(k+1)%len(loop)][2]-loop[k][2])%n
            if d>n//2:d-=n
            w+=d
        if w<0: loop=[(y,x,i) for (x,y,i) in reversed(loop)]
        bnd+=[(x,y) for (x,y,i) in loop]
    return cs,bnd
t=time.time(); cl=[gauss_lk(*curves(c),K=12) for c in pick]; t_cl=time.time()-t
agree=sum(1 for a,b in zip(ours,cl) if abs(float(a)-b)<0.05)
print(f"(Г) полуобороты: {len(pick)} лент; наш {t_ours:.2f} с (точно, дробями); интеграл Гаусса {t_cl:.2f} с (приближённо); совпало {agree}")
# ---------- (Д) потеря при сжатии: наша оценка мгновенно против точного перебора прообразов ----------
def compress_row(cells,a,f): return frozenset(a+(c-a)//f for c in cells)
rnd=random.Random(3); rows=[]
for L in (8,12,16,20):
    zone=list(range(L)); cells=frozenset(c for c in zone if rnd.random()<.6)|{0}
    f=2; a=0
    t=time.time()
    blocks={}
    for c in cells: blocks.setdefault((c-a)//f,[]).append(c)
    d=len(cells)-len(blocks); bound=2**d; tb=time.time()-t
    t=time.time(); res=compress_row(cells,a,f); cnt=0
    for m in range(1<<L):
        X=frozenset(c for c in zone if m>>c&1)
        if X and min(X)==0 and compress_row(X,0,f)==res: cnt+=1
    te=time.time()-t
    rows.append((L,len(cells),d,bound,cnt,tb,te))
for r in rows: print(f"(Д) зона {r[0]}: клеток {r[1]}, исчезло {r[2]}; оценка ≥ {r[3]} прообразов за {r[5]*1e3:.2f} мс; точно {r[4]} за {r[6]:.2f} с")
# ---------- (Е) дыры после 300 растяжений: пересчёт против закона «растяжение не меняет дыр» ----------
H=S+'/holes3d/h.py'; HH={}; exec(open(H).read().split("random.seed(1)")[0],HH)
ring={(x,y,0) for x in range(3) for y in range(3)}-{(1,1,0)}
O=set(ring); t=time.time(); recomputed=[]
for step in range(300):
    ax=rnd.randrange(3); f=2
    a=min(c[ax] for c in O)
    O={tuple(a+f*(c[i]-a)+j if i==ax else c[i] for i in range(3)) for c in O for j in range(f)} if len(O)<4000 else O
    if step%30==0: recomputed.append(HH['formula'](O,max(max(c) for c in O)+1)[1])
t_re=time.time()-t
print(f"(Е) растяжения всего объекта: пересчёт дыр по ходу {t_re:.2f} с, ответы {set(recomputed)}; по закону (Утв. 16б, 31) — 0 с, ответ 1 без счёта")

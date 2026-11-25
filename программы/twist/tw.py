# Счёт полуоборотов замкнутой ленты из квадратов: число зацепления середины ленты с её краем.
import sys, random
from fractions import Fraction as Fr
sys.argv=['x','4']
import importlib.util
spec=importlib.util.spec_from_file_location('m',__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','glue','mobius2.py'))
src=open(spec.origin).read().split("best = None")[0]
M={}; exec(src,M)
sq_verts,edges,squares_with_edge,analyse=M['sq_verts'],M['edges'],M['squares_with_edge'],M['analyse']

def half_twists(cyc, w):
    n=len(cyc); V={s:sq_verts(*s) for s in cyc}
    cen=lambda s: tuple(Fr(sum(p[i] for p in V[s]),4) for i in range(3))
    core=[]; glued=set()
    for i in range(n):
        a,b=cyc[i],cyc[(i+1)%n]; E=(set(edges(V[a]))&set(edges(V[b]))).pop(); glued.add(E)
        p,q=tuple(E); core.append(cen(a)); core.append(tuple(Fr(p[k]+q[k],2) for k in range(3)))
    owner={}
    for i,sq in enumerate(cyc):
        for E in edges(V[sq]):
            if E not in glued: owner[E]=i
    # собираем край в замкнутые ломаные и ориентируем каждую «вдоль ленты»
    adjv={}
    for E in owner:
        for v in E: adjv.setdefault(v,[]).append(E)
    if any(len(l)!=2 for l in adjv.values()): raise ValueError("особая точка края")
    left=set(owner); bnd=[]
    while left:
        E0=left.pop(); a,b=tuple(E0); loop=[(a,b,owner[E0])]; cur=b
        while True:
            nxt=[E for E in adjv[cur] if E in left]
            if not nxt: break
            E=nxt[0]; left.discard(E); x,y=tuple(E); y = y if x==cur else x
            loop.append((cur,y,owner[E])); cur=y
        wind=0
        for k in range(len(loop)):
            d=(loop[(k+1)%len(loop)][2]-loop[k][2])%n
            if d>n//2: d-=n
            wind+=d
        if wind<0: loop=[(y,x,i) for (x,y,i) in reversed(loop)]
        bnd+= [(x,y) for (x,y,i) in loop]
    # проекция вдоль w: базис плоскости u1,u2
    def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    u1=cross(w,(Fr(1),Fr(0),Fr(0))); u2=cross(w,u1)
    dot=lambda a,b: sum(x*y for x,y in zip(a,b))
    pr=lambda p:(dot(p,u1),dot(p,u2),dot(p,w))
    tot=0
    cs=[(core[i],core[(i+1)%len(core)]) for i in range(len(core))]
    for (A,B) in cs:
        a,b=pr(A),pr(B)
        for (P,Q) in bnd:
            p,q=pr(P),pr(Q)
            # пересечение отрезков a-b и p-q на плоскости
            d=(b[0]-a[0])*(q[1]-p[1])-(b[1]-a[1])*(q[0]-p[0])
            if d==0: continue
            t=((p[0]-a[0])*(q[1]-p[1])-(p[1]-a[1])*(q[0]-p[0]))/d
            s=((p[0]-a[0])*(b[1]-a[1])-(p[1]-a[1])*(b[0]-a[0]))/d
            if not(0<=t<=1 and 0<=s<=1): continue
            if t in (0,1) or s in (0,1): raise ValueError("не общее положение")
            ha=a[2]+t*(b[2]-a[2]); hp=p[2]+s*(q[2]-p[2])
            sign=1 if d>0 else -1
            tot+= sign if ha>hp else -sign
    # сумма по всем пересечениям (обе стороны) = 2·Lk; пересечения одной кривой над другой считаем оба вида
    return Fr(tot,2)
W=[(Fr(1),Fr(3,7),Fr(5,11)),(Fr(2,3),Fr(1),Fr(7,13)),(Fr(3,5),Fr(5,17),Fr(1))]
def lk(cyc):
    vals=[]
    for w in W:
        try: vals.append(half_twists(cyc,w))
        except ValueError: pass
    return vals
# 1) пример из текста (7 квадратов) и плоское кольцо
mob=None
start=((0,0,0),(0,1))
def find(L,limit):
    out=[]
    def dfs(path,used):
        if len(out)>=limit: return
        cur=path[-1]
        for E in edges(sq_verts(*cur)):
            for nb in squares_with_edge(E):
                if nb==cur: continue
                if len(path)==L and nb==path[0]:
                    r=analyse(path)
                    if r and r[0]==0: out.append((list(path),r[1]))
                    continue
                if nb in used or len(path)>=L: continue
                if any(abs(c)>2 for c in nb[0]): continue
                used.add(nb);path.append(nb);dfs(path,used);path.pop();used.discard(nb)
    dfs([start],{start}); return out
total=0;bad=0;hist={}
for L in (7,8,9,10):
    strips=find(L,400)
    for cyc,orientable in strips:
        v=lk(cyc)
        ok=len(set(v))==1 and len(v)>=2
        tw=v[0]
        par_ok=(tw.denominator==1) and ((tw.numerator%2==0)==bool(orientable))
        total+=1
        if not(ok and par_ok): bad+=1; print("BAD",L,v,orientable)
        hist[(L,int(tw),bool(orientable))]=hist.get((L,int(tw),bool(orientable)),0)+1
print("лент:",total,"расхождений:",bad)
for k in sorted(hist): print(k,hist[k])

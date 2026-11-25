# Узел из рёбер сетки (k = 1, n = 3): отличаем трилистник от кольца по «картинке» — раскраска в 3 цвета.
import math
from fractions import Fraction as Fr
def lattice_curve(fn, s, steps=4000):
    pts=[]
    for i in range(steps):
        p=fn(2*math.pi*i/steps); q=tuple(round(s*c) for c in p)
        if not pts or q!=pts[-1]: pts.append(q)
    if pts[0]==pts[-1]: pts.pop()
    path=[]
    for i in range(len(pts)):
        a,b=list(pts[i]),pts[(i+1)%len(pts)]
        path.append(tuple(a))
        for ax in range(3):
            while a[ax]!=b[ax]:
                a[ax]+=1 if b[ax]>a[ax] else -1
                if tuple(a)!=b: path.append(tuple(a))
    # убрать возвраты и проверить, что кривая не пересекает сама себя
    changed=True
    while changed:
        changed=False
        for i in range(len(path)):
            if path[i]==path[(i+2)%len(path)]:
                del path[(i+1)%len(path)]; del path[i%len(path)]; changed=True; break
    assert len(set(path))==len(path), "самопересечение"
    return path
def crossings(path, w):
    n=len(path); W=tuple(Fr(x) for x in w)
    def cr(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    u1=cr(W,(Fr(1),Fr(0),Fr(0))); u2=cr(W,u1); dot=lambda a,b: sum(x*y for x,y in zip(a,b))
    P=[(dot(p,u1),dot(p,u2),dot(p,W)) for p in path]
    res=[]   # (под-ребро i, параметр t на нём, над-ребро j)
    for i in range(n):
        a,b=P[i],P[(i+1)%n]
        for j in range(n):
            if abs(i-j)<=1 or {i,j}=={0,n-1}: continue
            p,q=P[j],P[(j+1)%n]
            d=(b[0]-a[0])*(q[1]-p[1])-(b[1]-a[1])*(q[0]-p[0])
            if d==0:
                # параллельные на виде: проверим, не лежат ли на одной прямой
                if (p[0]-a[0])*(b[1]-a[1])-(p[1]-a[1])*(b[0]-a[0])==0:
                    A,B,C,D=path[i],path[(i+1)%n],path[j],path[(j+1)%n]
                    ax=[k for k in range(3) if A[k]!=B[k]][0]
                    same=all(A[k]==C[k]==D[k] for k in range(3) if k!=ax) and C[ax]!=D[ax]
                    if not same: raise ValueError("вырожденный вид")
                continue
            t=((p[0]-a[0])*(q[1]-p[1])-(p[1]-a[1])*(q[0]-p[0]))/d
            s=((p[0]-a[0])*(b[1]-a[1])-(p[1]-a[1])*(b[0]-a[0]))/d
            if 0<=t<=1 and 0<=s<=1 and (t in (0,1) or s in (0,1)): raise ValueError("вырожденный вид")
            if 0<t<1 and 0<s<1:
                ha=a[2]+t*(b[2]-a[2]); hp=p[2]+s*(q[2]-p[2])
                if ha<hp: res.append((i,t,j,s))
    return res
def colorings(path,w):
    n=len(path); X=crossings(path,w)
    if not X: return 3, 0
    # разрезы кривой в нижних проходах -> дуги
    cuts=sorted((i+t) for i,t,j,s in X)
    def arc(pos):  # номер дуги, в которой лежит позиция pos вдоль кривой
        k=sum(1 for c in cuts if c<pos); return k%len(cuts)
    m=len(cuts); rows=[]
    for i,t,j,s in X:
        under_in=arc(i+t-1e-9) if False else None
        c=i+t; k=cuts.index(c)
        u1=k%m; u2=(k+1)%m           # дуга до разреза и после
        o=arc(j+s)
        r=[0]*m; r[u1]+=1; r[u2]+=1; r[o]-=2
        rows.append([x%3 for x in r])
    # ранг по модулю 3
    rank=0; cols=m; R=[r[:] for r in rows]
    for c in range(cols):
        piv=next((r for r in range(rank,len(R)) if R[r][c]%3),None)
        if piv is None: continue
        R[rank],R[piv]=R[piv],R[rank]; inv=1 if R[rank][c]==1 else 2
        R[rank]=[(x*inv)%3 for x in R[rank]]
        for r in range(len(R)):
            if r!=rank and R[r][c]: f=R[r][c]; R[r]=[(x-f*y)%3 for x,y in zip(R[r],R[rank])]
        rank+=1
    return 3**(m-rank), len(X)
tref=lambda t:(math.sin(t)+2*math.sin(2*t), math.cos(t)-2*math.cos(2*t), -math.sin(3*t))
circ=lambda t:(3*math.cos(t),3*math.sin(t),0.7*math.sin(2*t))
fig8=lambda t:((2+math.cos(2*t))*math.cos(3*t),(2+math.cos(2*t))*math.sin(3*t),math.sin(2*t))  # торический узел (3,2) = трилистник
import random
rnd=random.Random(7)
W=[]
while len(W)<5: W.append((Fr(rnd.randint(1,997),1009),Fr(rnd.randint(1,991),1013),Fr(rnd.randint(500,1019),1021)))
for name,fn in (("трилистник",tref),("кольцо",circ),("трилистник-2 (другая форма)",fig8)):
    for s in (3,5,8):
        try: path=lattice_curve(fn,s)
        except AssertionError as e: print(name,s,e); continue
        out=[]
        for w in W:
            try: out.append(colorings(path,w))
            except ValueError: out.append(('выр',0))
        print(f"{name}, масштаб {s}: {len(path)} рёбер; раскрасок (по 4 видам сбоку): {[o[0] for o in out]}, пересечений {[o[1] for o in out]}")

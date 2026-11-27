# Do zones that take only PART of a column let a relief be built in fewer raises than ceil(log2 D)?
# BFS over shapes in a W x H box from one cell: alpha with any zone (subset of current cells), P3, P5 (glues tracked).
import itertools, math, sys
sys.path.insert(0,'../anyfig'); from bfs import stretch, norm, contacts
W,H=int(sys.argv[1]),int(sys.argv[2]);MAXD=int(sys.argv[3])
start=norm(frozenset({(0,0)}),set());depth={start[0]:0};seen={start};fr=[start]
for d in range(1,MAXD+1):
    nf=[]
    for c,g in fr:
        cl=list(c)
        for k in range(1,len(cl)+1):
            for Z in itertools.combinations(cl,k):
                Z=frozenset(Z)
                for axis in (0,1):
                    for s in (1,-1):
                        for f in range(2,(W if axis==0 else H)+1):
                            r=stretch(c,g,Z,axis,s,f)
                            if not r:continue
                            nc,ng=norm(*r)
                            if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H:continue
                            key=(nc,frozenset(ng))
                            if key in seen:continue
                            seen.add(key);nf.append(key)
                            if nc not in depth:depth[nc]=d
    fr=nf;print('depth',d,'states',len(fr),flush=True)

import itertools as it
def R(H):
    H=sorted(set(h for h in H if h>1))
    if not H: return 0
    C=set(H)
    for a,b in it.combinations(H,2):
        g=math.gcd(a,b)
        C|={d for d in range(2,g+1) if g%d==0}
    C|={h//d for h in H for d in list(C) if h%d==0 and h//d>=2}
    C=sorted(C)
    for k in range(1,len(H)+1):
        for M in it.combinations_with_replacement(C,k):
            pr=set()
            for r in range(1,k+1):
                for S in it.combinations(M,r): pr.add(math.prod(S))
            if all(h in pr for h in H): return k

def side_heights(c):
    # высоты со всех четырёх сторон; None, если с этой стороны фигура не рельеф
    out=[]
    xs=sorted({x for x,y in c}); ys=sorted({y for x,y in c})
    for axis in (0,1):
        lines=ys if axis==0 else xs
        for side in (0,1):
            hs=[];ok=True
            for L in lines:
                pts=sorted(p[axis] for p in c if p[1-axis]==L)
                lo,hi=(min(xs),max(xs)) if axis==0 else (min(ys),max(ys))
                if pts!=list(range(pts[0],pts[-1]+1)): ok=False;break
                if side==0 and pts[0]!=lo: ok=False;break
                if side==1 and pts[-1]!=hi: ok=False;break
                hs.append(len(pts))
            if ok and len(lines)>=2: out.append(hs)
    return out
less=more=eq=0; ex=[]
for c,d in depth.items():
    xs={x for x,y in c};w=max(xs)+1
    if xs!=set(range(w)) or w<2: continue
    h=[0]*w;ok=True
    for x in range(w):
        ys=sorted(y for xx,y in c if xx==x)
        if ys!=list(range(len(ys))):ok=False;break
        h[x]=len(ys)
    if not ok: continue
    f=min(1+R(hs) for hs in side_heights(c))
    if d<f: less+=1; ex.append((h,d,f))
    elif d>f: more+=1; ex.append((h,d,f))
    else: eq+=1
print("совпало",eq,"быстрее формулы",less,"дольше формулы",more)
for e in ex[:15]: print(e)

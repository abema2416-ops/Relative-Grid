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

W,H=int(sys.argv[1]),int(sys.argv[2])
def lines_of(c,axis):
    d={}
    for p in c: d.setdefault(p[1-axis],[]).append(p[axis])
    return d
def normc(c):
    mx=min(x for x,y in c); my=min(y for x,y in c)
    return frozenset((x-mx,y-my) for x,y in c)
def steps(c):
    out=set()
    for axis in (0,1):
        L=lines_of(c,axis)
        for sgn in (1,-1):
            # группы линий с общим началом (якорем) a; каждая линия — сплошной отрезок
            starts={}
            for k,v in L.items():
                if sorted(v)!=list(range(min(v),max(v)+1)): continue
                a=min(v) if sgn==1 else max(v)
                starts.setdefault(a,[]).append(k)
            for a,good in starts.items():
                for r in range(1,len(good)+1):
                    for S in itertools.combinations(good,r):
                        for kind in ("mul","add"):
                            for f in range(1,max(W,H)+1):
                                if kind=="mul" and f<2: continue
                                nc=set(c); bad=False
                                for k in S:
                                    ln=len(L[k]); newlen= ln*f if kind=="mul" else ln+f
                                    for t in range(ln,newlen):
                                        p=[0,0]; p[axis]=a+sgn*t; p[1-axis]=k
                                        p=tuple(p)
                                        if p in c: bad=True
                                        nc.add(p)
                                if bad: continue
                                nc=normc(nc)
                                if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H: continue
                                out.add(nc)

            # третий вид шага: «раздвинуть» — целые линии (можно с промежутками) растягиваются по формуле α от общего якоря
            starts2={}
            for k,v in L.items():
                a=min(v) if sgn==1 else max(v)
                starts2.setdefault(a,[]).append(k)
            for a,good in starts2.items():
                for r in range(1,len(good)+1):
                    for S in itertools.combinations(good,r):
                        G=[p for p in c if p[1-axis] in S]
                        rest=set(c)-set(G)
                        for f in range(2,max(W,H)+1):
                            nc=set(rest); bad=False
                            for p in G:
                                t=sgn*(p[axis]-a)
                                for j in range(f):
                                    q=list(p); q[axis]=a+sgn*(f*t+j); q=tuple(q)
                                    if q in rest: bad=True
                                    nc.add(q)
                            if bad: continue
                            nc=normc(nc)
                            if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H: continue
                            out.add(nc)
    return out
mixed={frozenset({(0,0)}):0}; fr=[frozenset({(0,0)})]
for d in range(1,4):
    nf=[]
    for c in fr:
        for nc in steps(c):
            if nc not in mixed: mixed[nc]=d; nf.append(nc)
    fr=nf
less=more=eq=0; ex=[]; nores=0
import collections
for c,d in depth.items():
    if len(c)<2: continue
    f=mixed.get(frozenset(c),None)
    if f is None: f=99
    if d<f:
        less+=1
        if len(ex)<12: ex.append((sorted(c),d,f))
    elif d>f: more+=1
    else: eq+=1
print("ВСЕ ФИГУРЫ: совпало",eq,"реально быстрее модели",less,"модель обещает меньше",more)
def show(c):
    W2=max(x for x,y in c)+1;H2=max(y for x,y in c)+1
    return "\n".join("".join("█" if (x,y) in c else "·" for x in range(W2)) for y in range(H2-1,-1,-1))
for c,d,f in ex[:6]: print("действий",d,"модель",f); print(show(set(c))); print()
